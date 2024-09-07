from django.db import models

class Task(models.Model):
    # Choices for priority and status fields
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    # Fields for the Task model
    title = models.CharField(max_length=100)  # Title of the task
    description = models.TextField()  # Detailed description of the task
    due_date = models.DateField()  # Due date for the task
    priority = models.IntegerField(choices=PRIORITY_CHOICES)  # Priority level
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Current status

    def __str__(self):
        return self.title  # Return the title of the task as its string representation

