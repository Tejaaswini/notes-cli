# NOTES CLI App

A simple, interactive command-line tool to add, review, and manage notes and todos.

## Features
- Add notes and todos from the command line or interactive menu
- View notes by period (today, this week, etc.) or by tag (e.g., todo)
- Interactive menu for easy navigation
- SQLite-backed storage (local file)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd review_and_append
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies and the CLI tool:**
   ```bash
   pip install -e .
   ```

## Usage

### Command Line

Add a note:
```bash
notes "Remember to call mom"
```

Add a todo:
```bash
notes "Buy groceries" --tag todo
```

View today's notes:
```bash
notes today
```

View all todos:
```bash
notes todo
```

View notes for a period:
```bash
notes "this week"
notes "15 days"
notes "a month"
notes all
```

### Interactive Menu
Just run:
```bash
notes
```
And use the arrow keys to select actions like Add TODO, Add Note, View Notes, etc.

## Data Storage
- Notes are stored in a local SQLite database file: `notes.db`

## Uninstall
```bash
pip uninstall notes-app
```
