---
name: getcode
description: Fetch AtCoder competitive programming solutions and problem statements, then organize them into a contest directory. Use when the user wants to add solutions for an AtCoder contest (ABC, ARC, etc.), create contest directories, fetch submission code or problem descriptions from AtCoder, or organize CP solution files.
---

# Get AtCoder Code & Problems

Fetch AtCoder submission code and problem statements, then organize them into a contest directory.

## Workflow

### 1. Determine scope

Ask the user which contest and which problems they want to add (e.g., "ABC453, problems C and D").

### 2. Create contest directory

Create a directory named after the contest (e.g., `ABC453/`).

### 3. Fetch problem statements

For each problem, fetch the task page to understand the problem:

```
https://atcoder.jp/contests/<contest>/tasks/<contest>_<lowercase_letter>
```

Example: `https://atcoder.jp/contests/abc453/tasks/abc453_c`

Use `FetchURL` to get the problem description. Read and understand the problem statement before organizing the solution.

### 4. Fetch code from AtCoder submission

Ask the user for the submission URL. The URL format is:

```
https://atcoder.jp/contests/<contest>/submissions/<submission-id>
```

Example: `https://atcoder.jp/contests/abc453/submissions/74973690`

Fetch the submission page with `FetchURL` and extract the source code from the `Source Code` section.

**Note**: AtCoder submission detail pages are publicly accessible. Submission *list* pages (with filters) require login and cannot be scraped.

### 5. Alternative: Fetch via AtCoder Problems API

If the user provides an AtCoder username and wants to auto-discover their submissions, use the **AtCoder Problems API**:

```
https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=<username>&from_second=<unix_timestamp>
```

**Python example:**
```python
import requests
url = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"
params = {"user": "bnu2020", "from_second": 0}  # from_second is a Unix timestamp
r = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
data = r.json()  # List of submission objects
for s in data:
    print(s["contest_id"], s["problem_id"], s["id"], s["result"])
```

Each submission object contains:
- `id` — submission ID (use to build AtCoder detail URL)
- `contest_id` — e.g., `abc454`
- `problem_id` — e.g., `abc454_c`
- `result` — `AC`, `WA`, `TLE`, etc.

Filter by `contest_id` and `problem_id`, then fetch the accepted submission detail page to extract the source code.

**Note**: The API returns the most recent 500 submissions by default. Use a later `from_second` timestamp to paginate forward in time.

### 6. Write solution file

Create a file named `<lowercase_letter>.cpp` in the contest directory and write the extracted code. Preserve the original code as-is (including comments and formatting).

Example file layout:

```
ABC453/
├── c.cpp
└── d.cpp
```

### 7. Verify

List the directory to confirm files were created correctly.
