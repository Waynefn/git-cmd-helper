# git-cmd-helper

git-ch.py: A git command helper for fast branch checkout.
alias: Some alias for git.

## Dependency

- getch: 1.0

## How to use

1. Clone the git
2. Copy this py file to somewhere
3. Set a alias for this script, like

```
alias git-ch="python3 /Users/{User}/Projects/scripts/git-ch.py"
```

## Usage

- `git-ch`: Show a list and input the character in the square box to quickly check out a branch

```
[0] master
[1] ISSUE-001
[2] ISSUE-002
[3] ISSUE-003
```

(press `q` to cancel the selection)

- `git-ch -`: Check out last checked out branch
- `git-ch partial_name`: Check out a branch by partial match the branch name
- `git-ch a b ... `: Similar to `git checkout a b ...`
