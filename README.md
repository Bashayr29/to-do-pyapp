# To-Do PyApp

A minimal desktop To-Do list application built with Python and Tkinter. No external dependencies — stdlib only.

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
| `render_todos()` | Rebuilds the widget list after every state mutation |
| Scrollable canvas | Tkinter `Canvas` + `Scrollbar` wrapping the todo list frame |

## Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12 | Runtime |
| Tkinter | stdlib | GUI framework |
| python3-tk | system pkg | Tkinter backend (Ubuntu/Debian) |

## Run

```bash
# Install system dependency once (Ubuntu/Debian)
sudo apt-get install -y python3-tk

python todo.py
```

## Features

- Add tasks by typing in the input field and pressing **Enter** or clicking **Add**
- Delete individual tasks with the **Delete** button
- Scrollable task list for long to-do lists

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'tkinter'` | `sudo apt-get install -y python3-tk` |
| Window does not appear in CI | Use `xvfb-run python todo.py` |
| Scrollbar unresponsive on Linux | Use `<Button-4>`/`<Button-5>` events instead of `<MouseWheel>` |
