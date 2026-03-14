---
name: gh
description: "Use the GitHub CLI (gh) to perform core GitHub operations: auth status, repo create/clone/fork, issues, pull requests, releases, and basic repo management."
---

# GitHub CLI (gh)

## Overview
Use gh for authenticated GitHub operations from the terminal.

## Quick checks
- Auth status: gh auth status
- Current repo context: gh repo view --json nameWithOwner,url,defaultBranchRef

## Core workflows

### Repo create (private by default)
gh repo create OWNER/NAME --private --confirm --description "..."

### Clone / fork
gh repo clone OWNER/NAME
gh repo fork OWNER/NAME --clone

### Issues
- List: gh issue list --limit 20
- Create: gh issue create --title "..." --body "..."
- Comment: gh issue comment <num> --body "..."

### Pull requests
- Create: gh pr create --title "..." --body "..."
- List: gh pr list --limit 20
- View: gh pr view <num> --web
- Merge: gh pr merge <num> --merge

### Releases
gh release create vX.Y.Z --title "vX.Y.Z" --notes "..."
