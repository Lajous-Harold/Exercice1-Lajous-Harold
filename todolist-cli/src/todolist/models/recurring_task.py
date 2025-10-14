class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'incomplete'

    def mark_complete(self):
        self.status = 'complete'

    def __str__(self):
        return f"{self.title}: {self.description} [{self.status}]"


class RecurringTask(Task):
    def __init__(self, title, description, frequency):
        super().__init__(title, description)
        self.frequency = frequency

    def get_next_occurrence(self):
        # Logic to calculate the next occurrence based on frequency
        pass

    def __str__(self):
        return f"{super().__str__()} (Recurring every {self.frequency})"