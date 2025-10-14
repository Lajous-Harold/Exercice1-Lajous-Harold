class CLIView:
    def __init__(self, controller):
        self.controller = controller

    def display_tasks(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    def add_task(self, title, description=""):
        if not title:
            print("Title is required.")
            return
        self.controller.add_task(title, description)
        print(f"Task '{title}' added.")

    def remove_task(self, index):
        if self.controller.remove_task(index):
            print(f"Task {index} removed.")
        else:
            print(f"Task {index} not found.")

    def complete_task(self, index):
        if self.controller.mark_task_complete(index):
            print(f"Task {index} marked as complete.")
        else:
            print(f"Task {index} not found.")

    def display_help(self):
        print("""
ToDoList CLI - Commandes disponibles :
  add <titre> [description]   Ajouter une tâche
  list                       Afficher toutes les tâches
  remove <id>                Supprimer une tâche
  complete <id>              Marquer une tâche comme complétée
  help                       Afficher cette aide
        """)