# main.py

import sys
from pathlib import Path

# Add parent directory to sys.path when running directly
if __name__ == "__main__":
    file_path = Path(__file__).resolve()
    parent_path = str(file_path.parent.parent)
    if parent_path not in sys.path:
        sys.path.insert(0, parent_path)

from todolist.controllers.task_controller import TaskController
from todolist.views.cli_view import CLIView

def main():
    controller = TaskController()
    view = CLIView(controller)

    if len(sys.argv) < 2:
        view.display_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: add <titre> [description]")
            return
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        view.add_task(title, description)
    elif command == "list":
        view.display_tasks()
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: remove <id>")
            return
        task_id = sys.argv[2]
        view.remove_task(task_id)
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Usage: complete <id>")
            return
        task_id = sys.argv[2]
        view.complete_task(task_id)
    elif command == "help":
        view.display_help()
    else:
        print(f"Commande inconnue: {command}")
        view.display_help()

if __name__ == "__main__":
    main()