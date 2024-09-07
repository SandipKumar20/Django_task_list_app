from django.shortcuts import render
from .models import Task

def task_list(request):
    # Get the status filter and sorting option from the request parameters
    status_filter = request.GET.get('status')
    sort_by = request.GET.get('sort_by', 'priority')  # Default sorting by priority

    # Query all tasks from the database
    tasks = Task.objects.all()

    # Apply filtering if a status filter is provided
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Apply sorting based on the selected sorting option
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    else:
        tasks = tasks.order_by('priority')

    # Pass the filtered and sorted tasks to the template
    context = {
        'tasks': tasks,
    }

    return render(request, 'tasks/task_list.html', context)  # Render the template with context

