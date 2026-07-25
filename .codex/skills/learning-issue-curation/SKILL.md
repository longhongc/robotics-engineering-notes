---
name: learning-issue-curation
description: Capture and curate GitHub learning-record issues into the robotics textbook. Use when creating a learning issue, reviewing or processing a specific issue, reviewing the ready queue, appending learning comments, preparing a draft pull request, or completing an issue after a merged pull request.
---

# Learning Issue Curation

Use GitHub Issues as the intermediate learning archive and this repository as the permanent textbook. The issue body is the initial structured snapshot; comments are chronological continuation. Synthesize both. Never assume one issue becomes one note.

## Modes and commands

Support requests such as:

```text
Review learning issue #14
Process learning issue #14
Process the oldest open issue labeled curation:ready
Review all ready learning issues without changing files
Continue curation after receiving user feedback
```

Review-only mode is read-only and is the default for “review”, “dry-run”, or “without changing”. It may read GitHub and the repository but must not edit files, create branches, create or update pull requests, add comments, change labels, or change issue state. Setup work must not process existing learning issues.

Use the GitHub connector first for issues, comments, pull requests, labels, and repository data. Use local `git` and `gh` for checkout state, branch/PR discovery, commits, pushes, and gaps in connector coverage. Verify authentication before writes; never store tokens, cookies, or auth state in the repository.

## Unambiguous learning-record classifier

Treat an issue as a learning record only when it has:

1. `type:learning-record`; and
2. exactly one of `curation:archive-only`, `curation:review-later`, or `curation:ready`.

Ignore confidence, topic, processing, and other labels for classification. Ordinary issues are never learning records. If the permanent label is missing, or the issue has zero or multiple curation labels, stop and report the label problem rather than guessing.

For a specific issue, fetch it and verify it is open unless the user explicitly asks to revisit a closed issue. For queue processing, search only open issues with both `type:learning-record` and `curation:ready`, ordered oldest first unless the user requests another order. `curation:archive-only` and `curation:review-later` are not queue candidates.

Interpret curation labels as follows:

- `curation:archive-only`: preserve the learning record; do not select it automatically and keep it open unless explicitly concluded otherwise.
- `curation:review-later`: skip during normal processing; it needs more learning, evidence, or implementation.
- `curation:ready`: inspect the repository and decide the integration strategy. It does not imply creating a new note.

## Read the complete record

Before making a curation decision, read:

- issue title, body, state, labels, timestamps, and links;
- every issue comment, in chronological order;
- meaningful edits or updates exposed by the available tools;
- explicitly linked learning issues when materially relevant;
- linked pull requests and their current state;
- repository notes, indexes, scripts, and workflow files related to the subject.

Treat newer comments as later evidence without erasing earlier reasoning. Comments may contain corrections, implementation results, changed understanding, examples, open questions, cross-links, or user feedback. If the record remains too incomplete to curate responsibly, do not guess: explain the missing context in a comment only during an authorized processing run, leave the issue open, and do not create a PR.

If the issue contains a private ChatGPT source link, attempt to read it only through an authorized tool. Do not block on inaccessible private conversations; the issue body and comments are authoritative.

## Repository inspection and decision

Inspect the current repository before proposing edits. Search for:

- existing note titles and overlapping concepts;
- duplicate or conflicting explanations;
- related folders and neighboring topics;
- prerequisite and related notes;
- relevant generated files, indexes, scripts, tests, CI, and prior pull requests.

The issue taxonomy is independent from the textbook taxonomy. Classify content semantically and choose the folder where a future reader would look. Do not map issue wording or topics mechanically to folders. See `references/repository-profile.md` for the current baseline, but recheck it every run.

Choose one explicit implementation strategy:

- create a new independent note;
- update one existing note;
- update several existing notes;
- merge content from multiple learning issues;
- split one issue across multiple notes;
- add examples to one note and theory to another;
- defer publication with a concrete reason; or
- conclude the material is already adequately covered.

Prefer coherent existing notes over narrow duplicates. Explain the decision, central knowledge contribution, related repository notes, related learning issues, included/deferred material, uncertainties, and folder rationale before or alongside edits. The pull request must include this reasoning.

## Authorized textbook processing

Only after the user authorizes processing:

1. Check existing branches, pull requests, issue comments, and issue references for prior curation. Resume compatible work; do not create competing changes.
2. Start from the current default branch and create a stable branch such as `learning/<issue-number>-<slug>`.
3. Edit canonical Markdown under `raws/`; do not paste the issue body directly into a note.
4. Regenerate `docs/notes/` with the repository generator and update indexes/navigation only when its conventions require it.
5. Run relevant checks, inspect the diff and rendered result when practical, and avoid unrelated cleanup.
6. Open a draft pull request. Reference the issue with `Relates to #<number>` and list the strategy, source/generated files, related issues, deferred material, uncertainties, and validation.
7. Add one curation comment to the issue after the draft PR exists. Include the decision, draft PR URL, files, related issues, deferred material, and human-review questions. Do not add processing-status labels and do not close the issue.

The final textbook content must stand alone, preserve assumptions and conditions, explain reasoning and intuition, use useful examples or failure modes, and remain consistent with repository terminology. Do not fabricate citations or sources.

## Completion after merge

Do not close an issue merely because a draft PR exists. After confirming the PR merged:

1. inspect the final merged files and checks;
2. comment with the merged PR, final source/published links, deviations from plan, and deferred material; and
3. close the learning issue as completed.

When material was intentionally not published, close only when the user or workflow explicitly concludes its lifecycle. If one issue was absorbed into another, explain that relationship in a comment before closing.

## Continuous comments

When asked to add an insight, read the issue and relevant comments first, then append a natural-language comment without rewriting the body or changing labels unless explicitly requested. Identify the addition as an implementation update, correction, connection, new question, evidence, or changed interpretation. Preserve context and chronological evolution.

Follow linked issues selectively. Read linked learning records when they can change the integration decision; distinguish them from ordinary issues and do not recursively traverse every incidental link. Preserve relevant issue references in PR descriptions and issue comments.

## Idempotency and conflict handling

Before editing, search for:

- an existing branch or pull request tied to the issue number or title;
- a prior curation or completion comment;
- commits and changed files representing the same material;
- related learning issues already absorbed into another change.

Do not create duplicate notes, branches, PRs, or comments. If another curation process appears active, stop and report the conflict. Do not use processing labels as locks; visibility comes from branches, PRs, comments, and issue references.

## Labels and issue creation

Keep exactly these four labels available:

- `type:learning-record` — Learning summary created from a ChatGPT discussion.
- `curation:archive-only` — Preserve as a learning record without automatic textbook curation.
- `curation:review-later` — Revisit after further learning, evidence, or implementation.
- `curation:ready` — Ready for Codex to evaluate for textbook integration.

Do not create confidence, topic, or processing-status labels. Do not alter unrelated labels. If a label is missing, report the exact name and description and ask for setup; do not silently substitute another label.

When creating a learning issue, use the permanent type label and exactly one curation label. Keep the body concise but useful, with sections for session summary, current understanding, key concepts, misconceptions or fragile points, examples/robotics relevance, connections, open questions, source link when available, and curation intent. Later learning belongs in comments.

## Dry-run report

For review-only mode, report:

1. issue identity, state, labels, and classifier result;
2. complete-thread summary, including meaningful comment evolution;
3. related learning issues and linked PRs considered;
4. repository notes and duplicate/conflict evidence;
5. proposed integration strategy and semantic folder placement;
6. material to include, defer, or verify;
7. intended files, regeneration, and validation commands; and
8. idempotency, missing-context, authentication, or label blockers.

Make no repository, issue, label, branch, commit, push, or pull-request changes in this mode.

## Constraints

- Never process or publish learning issues during workflow setup.
- Never close an issue before merge confirmation or an explicit lifecycle conclusion.
- Never assume one issue maps to one note.
- Never depend on a private ChatGPT URL.
- Never create a GitHub Project board unless explicitly requested.
- Never introduce topic, confidence, or processing labels.
