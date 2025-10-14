from todolist.models.task import Task
from todolist.storage.json_storage import JSONStorage

class TaskController:
    def __init__(self, storage_file='tasks.json'):
        self.storage = JSONStorage(storage_file)
        self.storage.load()

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.storage.add_task(self._task_to_dict(task))
        self.storage.save()

    def remove_task(self, index):
        tasks = self.storage.get_tasks()
        try:
            index = int(index) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                self.storage.tasks = tasks
                self.storage.save()
                return True
            return False
        except (ValueError, IndexError):
            return False

    def list_tasks(self):
        return [self._dict_to_task(t) for t in self.storage.get_tasks()]

    def mark_task_complete(self, index):
        tasks = self.storage.get_tasks()
        try:
            index = int(index) - 1
            if 0 <= index < len(tasks):
                tasks[index]['completed'] = True
                self.storage.tasks = tasks
                self.storage.save()
                return True
            return False
        except (ValueError, IndexError):
            return False

    def _task_to_dict(self, task):
        return {
            'title': task.title,
            'description': task.description,
            'completed': getattr(task, 'completed', False)
        }

    def _dict_to_task(self, d):
        task = Task(d['title'], d.get('description', ""))
        task.completed = d.get('completed', False)
        return task