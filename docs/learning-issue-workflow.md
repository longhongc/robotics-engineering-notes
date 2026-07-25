# GitHub learning-issue workflow

GitHub Issues are the intermediate archive for learning discussions. The issue body is the initial structured learning summary; later comments preserve corrections, implementation results, examples, questions, and changed understanding. The repository under `raws/` remains the permanent textbook source.

The repository-local Codex skill at `.codex/skills/learning-issue-curation/SKILL.md` reads the complete issue thread and related repository context before deciding how knowledge should be integrated. One learning issue does not necessarily become one textbook note.

## Required labels

A learning record must have `type:learning-record` and exactly one curation label:

- `curation:archive-only` — preserve the record; do not select it automatically.
- `curation:review-later` — skip until the material matures.
- `curation:ready` — ready for Codex to inspect the repository and choose an integration strategy.

Do not use confidence, topic, or processing-status labels for classification. Ordinary issues are ignored.

The repository currently has GitHub’s default labels but not these four learning labels. Create them in the repository’s Issues → Labels page with the names and descriptions above before creating learning records. The setup does not create or process issues automatically.

## Roles and lifecycle

ChatGPT or a human captures the learning context in the issue body and appends later information as comments. Codex later reads the entire thread, linked learning issues and pull requests, and relevant `raws/` notes.

For `curation:ready`, Codex may create a note, update one or more notes, merge several issues, split one issue across notes, conclude the material is already covered, or defer publication. The decision is semantic and repository-aware; issue topics and wording are not folder mappings.

Codex opens a draft pull request and comments on the issue with the decision, PR, affected files, related issues, deferred material, and review questions. The issue stays open while the PR is under review. After confirming the PR merged, Codex adds the final links and closes the issue. A draft PR never closes an issue.

`curation:archive-only` and `curation:review-later` remain open by default. They are not processed by the normal ready queue.

## Review and processing requests

Examples:

```text
Review learning issue #14
Process learning issue #14
Process the oldest open issue labeled curation:ready
Review all ready learning issues without changing files
Continue curation after receiving user feedback
```

Review or dry-run mode makes no file, branch, pull-request, comment, label, or issue-state changes. Processing mode requires explicit authorization, checks for prior branches/PRs/comments, edits canonical source notes, regenerates derived docs, runs validation, and opens a draft PR.

Private ChatGPT source links are optional context. If they cannot be accessed, the issue body and comments remain authoritative; Codex must not block or invent missing content.

## Issue template

Use `.github/ISSUE_TEMPLATE/learning-record.md` for human-created records. It defaults to `curation:review-later`; change to exactly one curation label only after the record is mature enough for that editorial intent.
