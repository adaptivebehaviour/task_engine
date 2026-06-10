# Task Engine — Claude guidance

## Purpose

This repository is a **template workbench** for prototyping behavioural task mechanics. Developers copy it, then implement a specific task inside the copy. The goal at this stage is always correctness of the underlying logic (trial generation, response handling, scoring, adaptive rules), not UI polish.

## Running the app

```
streamlit run app.py
```

Or F5 in VS Code (uses `.vscode/launch.json` → `.vscode/app.bat`).

## Architecture

- **`app.py`** is the entire application. All task state lives in `st.session_state`. There is no database, no backend service, no separate model layer — keep it that way unless the task genuinely requires it.
- Streamlit re-runs `app.py` top-to-bottom on every interaction. Mutable state must be stored in `st.session_state`; local variables reset on each run.

## Conventions

- Use `@dataclass` for trial/result data structures (already imported).
- Keep task logic (generation, scoring, adaptive rules) in plain Python functions, not mixed into widget callbacks.
- `DEFAULT_MODEL` controls which task variant is active; `_reset_session()` is called when the variant changes.
- No comments unless the invariant would surprise a reader.

## What this repository is NOT for

- Do not implement specific tasks here. This repo is the template; tasks live in copies of it.
- Do not add persistence, authentication, or production infrastructure here.

## Testing

There are no automated tests yet. Verify task behaviour by running the app and working through representative trial sequences manually.
