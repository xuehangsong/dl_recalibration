# Project Template

Place this in your project root.

## project.md

```markdown
# {Project Name}

- **Project**: 
- **Run ID**: 
- **Mode**: (Research | Implementation | Review | Decision)
- **Started**: {YYYY-MM-DD}

## Goal

What are we trying to achieve?

## Scope

- **In-scope**: 
- **Out-of-scope**: 

## Current Status

- **Phase**: 
- **Last Update**: 

## Team

| Role | Owner | Since |
|------|-------|-------|
| PM | | |
| | | |

## Links

- Evidence: `./evidence/`
- Tasks: `./tasks.json`
- Handoff: `./handoff/`
```

## tasks.json

```json
{
  "version": "1.0",
  "project": "{project-name}",
  "tasks": [
    {
      "id": "001",
      "title": "",
      "owner": "",
      "eta": "",
      "status": "pending|in-progress|done|blocked",
      "evidence": "",
      "depends_on": []
    }
  ]
}
```

## Daily Update Format

```
Done | Next | Blocker | EvidenceRef | Owner | ETA
```

## Handoff Format

```markdown
# Handoff: {Task ID}

- **From**: {Role}
- **To**: {Role}
- **ETA**: {timestamp}
- **Inputs**: 
- **Outputs**: 
- **Evidence**: 
- **DoD**: 
```
