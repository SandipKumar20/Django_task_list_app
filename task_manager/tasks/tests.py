from django.test import TestCase
from .models import Task

class TaskListViewTests(TestCase):
    def setUp(self):
        # Create some sample tasks to test with
        Task.objects.create(title="Task 1", description="Task 1 description", due_date="2024-09-01", priority=1, status="To Do")
        Task.objects.create(title="Task 2", description="Task 2 description", due_date="2024-09-02", priority=2, status="In Progress")
        Task.objects.create(title="Task 3", description="Task 3 description", due_date="2024-09-03", priority=3, status="Done")

    def test_task_list_filtering_by_status(self):
        # Test that checks whether filtering by status is working correctly
        response = self.client.get('/tasks/?status=To Do')
        self.assertContains(response, "Task 1")  # Task 1 should be displayed
        self.assertNotContains(response, "Task 2")  # Task 2 should not be displayed
        self.assertNotContains(response, "Task 3")  # Task 3 should not be displayed

    def test_task_list_sorting_by_priority(self):
        # Test that checks whether sorting by priority is working correctly
        response = self.client.get('/tasks/?sort_by=priority')
        tasks = response.context['tasks']
        self.assertEqual(tasks[0].title, "Task 1")  # Task 1 should be first
        self.assertEqual(tasks[1].title, "Task 2")  # Task 2 should be second
        self.assertEqual(tasks[2].title, "Task 3")  # Task 3 should be third

    def test_task_list_sorting_by_due_date(self):
        # Test that checks whether sorting by due date is working correctly
        response = self.client.get('/tasks/?sort_by=due_date')
        tasks = response.context['tasks']
        self.assertEqual(tasks[0].title, "Task 1")  # Task 1 should be first by due date
        self.assertEqual(tasks[1].title, "Task 2")  # Task 2 should be second
        self.assertEqual(tasks[2].title, "Task 3")  # Task 3 should be third

