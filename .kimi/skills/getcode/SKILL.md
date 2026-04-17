---
name: atcoder-solutions
description: Manage an AtCoder competitive programming solution repository. Use when the user wants to add solutions for an AtCoder contest (e.g., ABC, ARC), create contest directories, fetch submission code from AtCoder, or organize CP solution files. The user handle is bnu2020, and solutions must use bnu2020's own code from AtCoder submissions.
---

# AtCoder Solutions Manager

Manage a personal AtCoder solution repository where each contest gets its own directory.

## User Info

- **Handle**: `bnu2020`
- **Code source**: AtCoder submission pages only

## Workflow

### 1. Determine scope

Ask the user which contest and which problems they want to add (e.g., "ABC453, problems C and D").

### 2. Create contest directory

Create a directory named after the contest (e.g., `ABC453/`).

### 3. Fetch code from AtCoder submission

For each problem, ask the user for the submission URL. The URL format is:

```
https://atcoder.jp/contests/<contest>/submissions/<submission-id>
```

Example: `https://atcoder.jp/contests/abc453/submissions/74973690`

Fetch the submission page with `FetchURL` and extract the source code from the `Source Code` section.

**Note**: AtCoder submission detail pages are publicly accessible. Submission *list* pages (with filters) require login and cannot be scraped.

### 4. Write solution file

Create a file named `<lowercase_letter>.cpp` in the contest directory and write the extracted code. Preserve the original code as-is (including comments and formatting).

Example file layout:

```
ABC453/
├── c.cpp
└── d.cpp
```

### 5. Verify

List the directory to confirm files were created correctly.
