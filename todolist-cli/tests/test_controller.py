from todolist.controllers.task_controller import TaskController
import unittest

class TestTaskController(unittest.TestCase):
    def setUp(self):
        self.controller = TaskController()

    def test_add_task(self):
        self.controller.add_task("Test Task", "This is a test task.")
        tasks = self.controller.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")

    def test_remove_task(self):
        self.controller.add_task("Test Task", "This is a test task.")
        self.controller.remove_task(0)
        tasks = self.controller.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks(self):
        self.controller.add_task("Test Task 1", "First test task.")
        self.controller.add_task("Test Task 2", "Second test task.")
        tasks = self.controller.list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_mark_complete(self):
        self.controller.add_task("Test Task", "This is a test task.")
        self.controller.mark_complete(0)
        tasks = self.controller.list_tasks()
        self.assertTrue(tasks[0].status)

if __name__ == '__main__':
    unittest.main()