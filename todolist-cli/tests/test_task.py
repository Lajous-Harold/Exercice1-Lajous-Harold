import unittest
from todolist.models.task import Task
from todolist.models.recurring_task import RecurringTask

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task(title="Test Task", description="This is a test task.")
        self.recurring_task = RecurringTask(title="Recurring Task", description="This task recurs daily.", frequency="daily")

    def test_task_initialization(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertFalse(self.task.is_complete)

    def test_mark_complete(self):
        self.task.mark_complete()
        self.assertTrue(self.task.is_complete)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), "Test Task - This is a test task. [Incomplete]")

    def test_recurring_task_initialization(self):
        self.assertEqual(self.recurring_task.title, "Recurring Task")
        self.assertEqual(self.recurring_task.description, "This task recurs daily.")
        self.assertEqual(self.recurring_task.frequency, "daily")

    def test_recurring_task_string_representation(self):
        self.assertEqual(str(self.recurring_task), "Recurring Task - This task recurs daily. [Incomplete] (Frequency: daily)")

if __name__ == '__main__':
    unittest.main()