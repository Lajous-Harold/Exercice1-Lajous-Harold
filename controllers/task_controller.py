from typing import List
from models.task import Task

class TaskController:
    def __init__(self):
        self._tasks: List[Task] = []

    def add_task(self, title: str, description: str = "") -> None:
        task = Task(title, description)
        self._tasks.append(task)

    def remove_task(self, index_zero_based) -> bool:
        try:
            idx = int(index_zero_based)
            if 0 <= idx < len(self._tasks):
                del self._tasks[idx]
                return True
            return False
        except (ValueError, IndexError):
            return False

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def complete_task(self, index_zero_based) -> bool:
        try:
            idx = int(index_zero_based)
            if 0 <= idx < len(self._tasks):
                self._tasks[idx].completed = True
                return True
            return False
        except (ValueError, IndexError):
            return False
