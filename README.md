# To-Do PyApp

A minimal desktop To-Do list application built with Python and Tkinter. No external dependencies — only the Python standard library.

## Architecture

```
to-do-pyapp/
├── todo.py          # Entire application: TodoApp class + __main__ entry point
└── .github/
    └── workflows/
        └── copilot-setup-steps.yml
```

| Component | Description |
|-----------|-------------|
| `TodoApp` | Single class owning all state (`self.todos`) and UI widgets |
| `render_todos()` | Rebuilds the widget list from scratch on every mutation |
| `add_todo()` | Validates input, appends to `self.todos`, re-renders |
| `delete_todo(index)` | Removes item by index, re-renders |

## Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12 | Runtime |
| Tkinter | stdlib | GUI framework |
| python3-tk | system pkg | Tkinter backend (Ubuntu/Debian) |

## Setup & Run

```bash
# Install system dependency (Ubuntu/Debian)
sudo apt-get install -y python3-tk

python todo.py
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'tkinter'` | Run `sudo apt-get install -y python3-tk` |
| App window does not appear in CI | Use `xvfb-run python todo.py` |
| Scrollbar not responding on Linux | Use `<Button-4>`/`<Button-5>` events instead of `<MouseWheel>` |
