# Python To-Do List

A simple command-line To-Do List application built with Python. This is my first real Python project, created to practice Python fundamentals, working with files, functions, and user input.

## Features

- **Create tasks** — Add new tasks to your to-do list.
- **List tasks** — View all your saved tasks.
- **Remove tasks** — Remove a task from your list.
- **Persistent storage** — Tasks are saved in a text file, so they remain available when you run the program again.
- **Help command** — See the available commands.

## Project Structure

```text
.
├── main.py       # Main program and command-line interface
├── utils.py      # Functions for loading, adding, and removing tasks
└── database.txt  # Stores tasks (created/used by the application)
```

## Requirements

- Python 3.10 or newer recommended
- No third-party packages required

## Getting Started

### 1. Clone or download the project

If you are using Git:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Alternatively, download the project files and open the project folder in your terminal.

### 2. Run the application

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

## Usage

After starting the program, enter a command at the prompt.

| Command | Description |
| --- | --- |
| `help` | Show the available commands |
| `list` | Display all tasks |
| `create <task>` | Add a new task |
| `remove <task>` | Remove a task by its exact text |
| `quit` | Exit the application |

### Example

```text
---Your To-do List---
Press help for list of commands
> create Finish Python project
Task created successfully
> create Read a book
Task created successfully
> list
1. Finish Python project
2. Read a book
> remove Read a book
Task removed successfully
> quit
Thankyou for using this program
```

## How It Works

- `main.py` displays the menu, accepts commands, and manages the application loop.
- `utils.py` contains helper functions to load tasks from a file, append new tasks, and rewrite the file when a task is removed.
- `database.txt` stores tasks, with one task per line.

## What I Learned

Through this project, I practiced:

- Python functions and modules
- Lists and loops
- User input and command handling
- Reading and writing text files
- Basic program organization

## Possible Future Improvements

- Add task numbers so tasks can be removed by number
- Mark tasks as completed
- Add due dates or priorities
- Handle missing or empty database files
- Improve command validation and error messages
- Add automated tests

## Author

Created by **Dashrath** as my first real Python project with multiple files.

---

If you find a bug or have a suggestion, feel free to open an issue or contribute!
