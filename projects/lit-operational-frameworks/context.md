# Project Context

## Latest Run

- **Date**: 2025-02-25
- **Run #**: 1
- **Status**: Complete

## History

## How to Use

This file serves as the "external session memory" for PM runs via Cron.

Each Cron run should:
1. Read this file for history
2. Append new entry after execution
3. Keep last 10 entries (prune older)

Format:
```
## YYYY-MM-DD HH:MM (Run #N)
- Completed: task-xxx
- Next: task-yyy
- Notes: ...
```
