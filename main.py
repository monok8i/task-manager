import json
import argparse
import datetime
import uuid


"""
    id: A unique identifier for the task
    description: A short description of the task
    status: The status of the task (todo, in-progress, done)
    createdAt: The date and time when the task was created
    updatedAt: The date and time when the task was last updated

"""


class Task:
    def __init__(
        self,
        description: str,
        id: str | None = None,
        status: str = "todo",
        createdAt: str | None = None,
        updatedAt: str | None = None,
    ) -> None:
        self.id = id if id is not None else str(uuid.uuid4())
        self.description = description
        self.status = status
        self.createdAt = (
            createdAt
            if createdAt is not None
            else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.updatedAt = (
            updatedAt
            if updatedAt is not None
            else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    def to_dict(self) -> dict:
        """Converts the Task object to a dictionary."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Creates a Task object from a dictionary."""
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"],
        )


class TaskManager:
    def __init__(self, filename: str):
        self.filename = filename
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Loads tasks from the JSON file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks: list[Task] = [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks: list[Task] = []

    def _save_tasks(self) -> None:
        """Saves tasks to the JSON file."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def _find_task(self, uuid: str) -> Task | None:
        """Finds a task by its UUID."""
        for task in self.tasks:
            if task.id == uuid:
                return task
        return None

    def create_task(self, description: str) -> None:
        """Creates a new task."""
        task = Task(description=description)
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added successfully: {task.id}")

    def update_task(self, uuid: str, new_description: str) -> None:
        """Updates an existing task's description."""
        task = self._find_task(uuid)
        if task:
            task.description = new_description
            task.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_tasks()
            print(f"Task with id {uuid} was successfully updated")
        else:
            print(f"Task with id {uuid} not found.")

    def delete_task(self, uuid: str) -> None:
        """Deletes a task."""
        task = self._find_task(uuid)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            print(f"Task with id {uuid} deleted successfully.")
        else:
            print(f"Task with id {uuid} not found.")

    def mark_task(self, uuid: str, new_status: str) -> None:
        """Marks a task with a new status."""
        task = self._find_task(uuid)
        if task:
            task.status = new_status
            task.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_tasks()
            print(f"Task with id {uuid} marked as {new_status}.")
        else:
            print(f"Task with id {uuid} not found.")

    def list_tasks(self, status: str = None):
        if not self.tasks:
            print("No tasks available.")
            return

        print("List of Tasks:")
        for task in self.tasks:
            if task.status == status:
                print(f"\n  - ID: {task.id}")
                print(f"    Description: {task.description}")
                print(f"    Status: {task.status}")
                print(f"    Created At: {task.createdAt}")
                print(f"    Updated At: {task.updatedAt}")
            else:
                print(f"\n  - ID: {task.id}")
                print(f"    Description: {task.description}")
                print(f"    Status: {task.status}")
                print(f"    Created At: {task.createdAt}")
                print(f"    Updated At: {task.updatedAt}")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument(
        "-f", "--filename", default="tasks.json", help="Task data filename (default: tasks.json)"
    )
    subparsers = parser.add_subparsers(
        title="commands", dest="command", help="Available commands"
    )

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new task")
    create_parser.add_argument("description", help="Description of the task")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", help="ID of the task to update")
    update_parser.add_argument("new_description", help="New description for the task")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", help="ID of the task to delete")

    # Mark command
    mark_parser = subparsers.add_parser("mark", help="Mark a task with a status")
    mark_parser.add_argument("id", help="ID of the task to mark")
    mark_parser.add_argument("status", help="New status for the task", choices=["in-progress", "todo", "done"])

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("-s", "--status", required=False, help="List all tasks that have this status", choices=["in-progress", "todo", "done"])


    args = parser.parse_args()
    tm = TaskManager(args.filename)

    match args.command:
        case "create":
            tm.create_task(args.description)
        case "update":
            tm.update_task(args.id, args.new_description)
        case "mark":
            tm.mark_task(args.id, args.new_status)
        case "list":
            tm.list_tasks(args.status)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
