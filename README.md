# To-Do App

A minimal desktop To-Do list application built with Python and Tkinter. No external dependencies — only the Python standard library is used.

## Features

- Add tasks by typing and pressing **Enter** or clicking **Add**
- Delete individual tasks with the **Delete** button
- Scrollable task list that handles any number of items
- Clean, lightweight UI with no third-party packages

## Requirements

- Python 3.12+
- `python3-tk` system package (Tkinter backend)

## Setup

```bash
# Install the Tkinter system dependency (Ubuntu/Debian)
sudo apt-get install -y python3-tk
```

## Run

```bash
python todo.py
```

> **Headless environments (e.g. CI):** Use a virtual display:
> ```bash
> xvfb-run python todo.py
> ```

## Project Structure

```
to-do-pyapp/
├── todo.py          # Entire application: TodoApp class + __main__ entry point
├── README.md
└── .github/
    └── workflows/
        └── copilot-setup-steps.yml
```

## Development

The entire application lives in `todo.py` — keep it that way unless complexity clearly justifies splitting.

**Linting (optional):**
```bash
pip install flake8
flake8 todo.py
```

**Type checking (optional):**
```bash
pip install mypy
mypy todo.py
```

**Tests** — place test files under `tests/test_*.py` and run with:
```bash
pip install pytest
pytest
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'tkinter'` | Run `sudo apt-get install -y python3-tk` |
| App window does not appear in CI | Use `xvfb-run python todo.py` |
| Scrollbar not responding on Linux | Replace `<MouseWheel>` with `<Button-4>`/`<Button-5>` events |
