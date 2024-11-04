# from django.shortcuts import render
# from .models import ToDoItem

# def index(request):
#     tasks = ToDoItem.objects.all()
#     return render(request, 'tasks/index.html', {'tasks': tasks})
from django.shortcuts import render
from django.utils import timezone
from .models import ToDoItem

# Index view
def index(request):
    tasks = ToDoItem.objects.all() 
    return render(request, 'tasks/index.html', {'tasks': tasks})

# View for today's tasks
def today_tasks(request):
    today = timezone.now().date()  # Get today's date
    tasks = ToDoItem.objects.filter(due_date=today)  # Filter tasks by today's date
    return render(request, 'tasks/today.html', {'tasks': tasks})
