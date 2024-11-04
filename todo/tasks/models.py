import datetime
from django.db import models

# Create your models here.
from django.utils import timezone

class ToDoItem(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now, blank=True)
    due_date = models.DateField(default=timezone.now) 

    def __str__(self):
        #return self.task
        return f"{self.task}: due {self.due_date}"