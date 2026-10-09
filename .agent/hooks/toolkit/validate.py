#!/usr/bin/env python3
"""Read-only structural validation for the repository agent toolkit."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print('UNAVAILABLE: toolkit validation requires Python 3 with PyYAML.', file=sys.stderr)
    sys.exit(2)

BASELINE = {'build', 'investigate', 'research', 'verify', 'review', 'fix',
            'release', 'deploy', 'publish', 'push', 'pull'}
CONTRACTS = {'core', 'authorization', 'verification', 'git-github',
             'deployment', 'handoff', 'memory', 'scopes'}
PROVIDERS = ('.agents/skills', '.claude/skills')
# Claude Code loads these adapters only on an explicit /name invocation.
CLAUDE_USER_ONLY = {'release', 'deploy', 'publish'}


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys instead of silently accepting drift."""


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    root = parser.parse_args().root.resolve()
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def load_yaml(path):
        return yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueLoader)

    def frontmatter(path, provider_fields=()):
        text = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        if not match:
            raise ValueError(f'{path.relative_to(root)}: missing YAML frontmatter')
        data = yaml.load(match.group(1), Loader=UniqueLoader)
        if not isinstance(data, dict):
            raise ValueError(f'{path.relative_to(root)}: frontmatter is not a mapping')
        require(set(data) == {'name', 'description', *provider_fields},
                f'{path.relative_to(root)}: unexpected frontmatter fields')
        require(data.get('name') == path.parent.name, f'{path.relative_to(root)}: name differs from directory')
        require(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(data.get('name', '')))),
                f'{path.relative_to(root)}: invalid skill name')
        require(isinstance(data.get('description'), str) and bool(data['description'].strip()),
                f'{path.relative_to(root)}: missing description')
        return data, text[match.end():]

    required = ['AGENTS.md', 'CLAUDE.md', '.agent/README.md', '.agent/project.yaml',
                '.agent/integrations/README.md', '.agent/workflows/README.md',
                '.agent/hooks/README.md', '.agent/evals/skill-routing.md',
                '.codex/skills/README.md', 'docs/agent-index.json']
    required += [f'.agent/contracts/{n}.md' for n in CONTRACTS]
    required += [f'skills/{n}/SKILL.md' for n in BASELINE]
    for name in required:
        require((root / name).is_file(), f'missing required file: {name}')
    if errors:
        raise ValueError('\n'.join(errors))

    metadata = load_yaml(root / '.agent/project.yaml')
    require(metadata['schema_version'] == 1, 'unsupported project schema')
    require(metadata['project'] == {'id': 'github:jikovec/Aetheris-UI', 'name': 'Aetheris UI',
                                   'type': 'documentation'}, 'project identity/type drift; reconcile accepted metadata')
    require(metadata['repository'] == {'host': 'github', 'owner': 'jikovec', 'name': 'Aetheris-UI',
                                      'default_branch': 'main', 'canonical_remote': 'origin'},
            'repository binding drift; verify live identity before changing the contract')
    require(metadata['organization'] == {'id': None, 'name': None}, 'unexpected organization binding')
    require(metadata['ownership'] == {'class': 'user-owned'}, 'unexpected ownership classification')
    require(metadata['mind_seed'] == {'enabled': False, 'binding': None},
            'Mind-Seed binding requires verified adoption and validator update')
    require(not (root / '.mind-seed').exists(), 'unexpected Mind-Seed files while binding is disabled')
    require(metadata['environment']['primary_runtime'] is None and
            metadata['environment']['package_manager'] is None, 'app runtime must come from actual manifests')
    for value in [*metadata['agent'].values(), metadata['integrations']['directory'],
                  metadata['workflows']['directory'], *metadata['environment']['source_files']]:
        require((root / value).exists(), f'unresolved metadata path: {value}')
    require(set(metadata) == {'schema_version', 'project', 'repository', 'organization',
                             'ownership', 'agent', 'environment', 'integrations', 'workflows', 'mind_seed'},
            'unexpected project metadata field; review for transient state')

    canonical = {}
    descriptions = set()
    for path in sorted((root / 'skills').rglob('SKILL.md')):
        data, _ = frontmatter(path)
        name = data['name']
        require(name not in canonical, f'canonical skill collision: {name}')
        require(data['description'] not in descriptions, f'duplicate skill description: {name}')
        canonical[name] = (path, data)
        descriptions.add(data['description'])
    require(BASELINE <= canonical.keys(), 'missing baseline skill')
    for provider in PROVIDERS:
        files = sorted((root / provider).glob('*/SKILL.md'))
        require({p.parent.name for p in files} == canonical.keys(), f'{provider}: adapter coverage differs')
        for path in files:
            gated = provider == '.claude/skills' and path.parent.name in CLAUDE_USER_ONLY
            data, body = frontmatter(path, ('disable-model-invocation',) if gated else ())
            if gated:
                require(data.pop('disable-model-invocation', None) is True,
                        f'{path.relative_to(root)}: Claude adapter must set disable-model-invocation: true')
            target, expected = canonical[path.parent.name]
            require(data == expected, f'{path.relative_to(root)}: frontmatter drift')
            relative = target.relative_to(root).as_posix()
            expected_body = (f'\nRead and follow the canonical workflow at [{relative}](../../../{relative}) before acting.\n'
                             'Also follow repository-root `AGENTS.md` and applicable scoped instructions.\n'
                             'This adapter provides discovery only; canonical workflow policy stays in that file.\n')
            require(body == expected_body, f'{path.relative_to(root)}: adapter differs from thin pointer contract')
    require(not list((root / '.codex/skills').rglob('SKILL.md')), 'duplicate Codex native adapter surface')
    require('@AGENTS.md' in (root / 'CLAUDE.md').read_text().splitlines(), 'missing Claude policy import')

    index = json.loads((root / 'docs/agent-index.json').read_text())
    require(index['agentToolkit']['projectId'] == metadata['project']['id'], 'machine index identity drift')
    require(set(index['agentToolkit']['contracts']) == CONTRACTS, 'machine index contract drift')
    require(index['agentToolkit']['mindSeedEnabled'] is False, 'machine index Mind-Seed drift')
    for value in [*index['importantPaths'].values(), *index['docsEntryPoints'], *index['toolingAreas']]:
        require((root / value).exists(), f'unresolved machine-index path: {value}')
    routing = (root / '.agent/evals/skill-routing.md').read_text()
    for name in canonical:
        rows = [line for line in routing.splitlines() if line.startswith(f'| {name} |')]
        require(len(rows) == 1 and len(rows[0].split('|')) == 8,
                f'{name}: routing requires one row with 3 positives and 2 counterexamples')

    # Scan only repository-owned documentation/tooling, never ignored user data.
    roots = ['.agent', '.agents/skills', '.codex/skills', '.claude/skills', 'skills',
             'docs', 'reports', 'handoffs', 'DOCUMENTATION']
    files = set(root.glob('*.md'))
    for directory in roots:
        files.update(p for p in (root / directory).rglob('*') if p.is_file() and p.suffix in {'.md', '.yaml', '.yml', '.json', '.py'})
    link_count = 0
    for path in sorted(files):
        text = path.read_text(encoding='utf-8')
        rel = path.relative_to(root)
        require(text.endswith('\n'), f'{rel}: missing final newline')
        require(not re.search(r'^\s*(?:<<<<<<< |=======\s*$|>>>>>>> )', text, re.M), f'{rel}: conflict marker')
        require(not re.search(r'[ \t]+$', text, re.M), f'{rel}: trailing whitespace')
        if path.suffix in {'.yaml', '.yml'}:
            load_yaml(path)
        elif path.suffix == '.json':
            json.loads(text)
        if path.suffix != '.md':
            continue
        # Inline Markdown links in prose; code examples and external URLs are excluded.
        prose = re.sub(r'^```.*?^```[^\n]*$', '', text, flags=re.M | re.S)
        for link in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', prose):
            target = link.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            require(dest.is_relative_to(root) and dest.exists(), f'{rel}: broken or escaping link: {target}')
            link_count += 1
    if errors:
        print('\n'.join('FAIL: ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(canonical)} canonical skills, {len(canonical) * len(PROVIDERS)} native adapters, '
          f'{len(files)} files, {link_count} local links; identity/index/routing structure consistent.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
