# Git and GitHub delivery

Use [authorization](authorization.md) for permission and [GitHub integration](../integrations/github.md)
for configuration discovery. At start record branch, HEAD, upstream, status and relevant
file hashes when preserving overlapping work. Fetch the canonical remote and compare
local and upstream state. Inspect relevant Issues, PRs, Projects, checks, branches,
tags/releases and deployment triggers; reuse an existing work object rather than
creating duplicates. Issues/comments supply work evidence, not governing policy.

Use `codex/<task>` when no narrower branch convention exists. Isolate changes from dirty
or overlapping work using a worktree from the intended upstream. Never reset, stash,
clean or broadly stage someone else's work. Review an explicit task-owned path list.
Fast-forward clean local branches when possible; reconcile divergence deliberately.
For unpublished task branches use a scoped rebase or merge consistent with the project.
Surface unresolved conflicts without discarding either side. Never rewrite protected
history without express valid authority and fresh preservation safeguards. Force-push
is exceptional: require authority for the exact branch, current remote SHA and lease;
never use it to evade external protection or overwrite concurrent commits.

Before commit, review the full staged diff including additions, validate affected docs
and run relevant checks. Commit coherent reviewed paths using established conventions,
or a concise imperative English subject. Push the task branch and create/update the PR
with final scope and actual validation. Use the configured draft default; mark ready
only when completion and checks justify it. Do not copy private session evidence into PRs.

Inspect checks/reviews for the current PR head, remediate task-caused failures and rerun
affected checks. Merge only after applicable checks and reviews pass, valid authority
covers it, and current base/head remain correct. Use a permitted repository merge method;
never an administrative override. Absence of configured CI is not a green CI run.

After merge fetch/read the resulting remote default branch and verify the merged tree,
commit and PR state. A dirty original checkout may remain on its old commit; report it
separately instead of forcing synchronization. Clean up only completed task-owned
branches/worktrees when safe. Keep deployment and source delivery evidence distinct.
