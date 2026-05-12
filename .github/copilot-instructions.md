# Copilot Instructions

## Project Overview

A minimal desktop To-Do list application built with Python and Tkinter. The entire application lives in a single file (`todo.py`). There are no external runtime dependencies — only the Python standard library is used.

## Architecture

```
to-do-pyapp/
├── todo.py          # Entire application: TodoApp class + __main__ entry point
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       └── copilot-setup-steps.yml  # Copilot cloud agent environment setup
└── .gitignore
```

- **`TodoApp`** – single class that owns all state (`self.todos` list) and all UI widgets (Tk root, entry, scrollable canvas, list frame).
- UI is re-rendered from scratch on every mutation via `render_todos()`.

## Technologies

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12 | Runtime |
| Tkinter | stdlib | GUI framework |
| python3-tk | system pkg | Tkinter backend (required on Ubuntu) |

## Run

```bash
# Install system dependency once (Ubuntu/Debian)
sudo apt-get install -y python3-tk

python todo.py
```

> Tkinter opens a native desktop window. Running in a headless environment (e.g. CI) requires a virtual display (e.g. `xvfb-run python todo.py`).

## Build, Lint, Test

There is no build step (pure Python). No test suite or linter configuration exists yet.

Recommended tools to add when introducing tests or linting:

```bash
# Linting
pip install flake8
flake8 todo.py

# Type checking
pip install mypy
mypy todo.py

# Tests (once a test file is added)
pip install pytest
pytest
```

## Development Conventions

- **Single-file rule**: keep all application code in `todo.py` unless the complexity clearly justifies splitting.
- **No external dependencies**: do not add third-party packages without a strong reason. Prefer stdlib.
- **Class structure**: add new features as methods on `TodoApp`. Keep `__main__` block minimal.
- **State**: all to-do items live in `self.todos` (a plain Python list). Persist state to a file if persistence is needed.
- **Re-render pattern**: after every state mutation, call `self.render_todos()` to rebuild the widget list. Avoid partial updates.
- **Style**: follow PEP 8. Use `("Helvetica", size)` font tuples for consistency with existing widgets.

## CI/CD

The only workflow is `.github/workflows/copilot-setup-steps.yml`, which prepares the Copilot cloud agent environment:

1. Checks out the repo
2. Sets up Python 3.12
3. Installs `python3-tk` via apt
4. Creates and activates a virtualenv

There are no automated test or lint jobs. Any new workflow added should follow the same pattern and run on `ubuntu-latest`.

## Pull Request Expectations

- Keep changes focused and minimal.
- Do not introduce external dependencies without updating `copilot-setup-steps.yml` to install them.
- If adding tests, place them in a `tests/` directory and name files `test_*.py`.
- Ensure `python todo.py --help` (or a dry-run import) does not raise errors before submitting.
- Describe what changed and why in the PR description.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'tkinter'` | Run `sudo apt-get install -y python3-tk` |
| App window does not appear in CI | Use `xvfb-run python todo.py` or skip GUI tests in headless environments |
| Scrollbar not responding | `<MouseWheel>` binding uses `e.delta // 120`; on Linux use `<Button-4>`/`<Button-5>` events instead |
