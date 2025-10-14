import json
import os

class JSONStorage:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_dict):
        self.tasks.append(task_dict)

    def get_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks = []