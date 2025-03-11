# Task Tracker CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a command-line interface (CLI) application for managing tasks. You can create, update, delete, mark, and list tasks.

This is also sample solution for the [task-manager](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## Features

*   **Create Tasks:** Add new tasks with descriptions.
*   **Update Tasks:** Modify the description of existing tasks.
*   **Delete Tasks:** Remove tasks from your list.
*   **Mark Tasks:** Change the status of tasks (e.g., todo, in-progress, done).
*   **List Tasks:** View all your tasks with their details.
*   **Data Persistence:** Tasks are stored in a JSON file (`tasks.json` by default).
*   **Customizable Data File:** You can specify a different JSON file for storing tasks.

## How to install

1.  **Python:** Ensure you have Python 3.10 or later installed on your system. You can check your Python version by running:

    ```bash
    python --version (or python3 if you are using linux/macOS)
    ```
2. **Clone repository:** Clone repository with this project to your local system
    ```bash
    git clone <your-repository>
    cd <your-repository-dir>
    ```

## Usage

### Basic Commands

The script is run using the `python` command followed by the `main.py` filename, and then a subcommand and any required arguments.

*   **Help:**
    ```bash
    python main.py --help
    ```
    This will display a list of available commands and options.

*   **Create a Task:**
    ```bash
    python main.py create "Buy groceries"
    ```
    This will create a new task with the description "Buy groceries."

*   **Update a Task:**
    ```bash
    python main.py update <task_id> "Buy organic groceries"
    ```
    Replace `<task_id>` with the actual ID of the task you want to update. This command updates the task's description.

*   **Delete a Task:**
    ```bash
    python main.py delete <task_id>
    ```
    Replace `<task_id>` with the ID of the task you want to delete.

*   **Mark a Task:**
    ```bash
    python main.py mark <task_id> in-progress
    ```
    Replace `<task_id>` with the ID of the task you want to mark. This command changes the task's status (e.g., `todo`, `in-progress`, `done`).

*   **List Tasks:**
    ```bash
    python main.py list
    ```
    This will display all your tasks with their IDs, descriptions, statuses, creation dates, and update dates.
    ```bash
    python main.py list -s <status>
    ```
    This will display all your tasks with specific status (e.g. `todo`, `in-progress`, `done`)


### Using a Custom Data File

By default, the application uses a file named `tasks.json` to store task data. You can specify a different filename using the `-f` or `--filename` option:

```bash
python main.py -f my_tasks.json list
