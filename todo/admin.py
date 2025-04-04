from django.contrib import admin
from .models import Task

# Register the ToDoItem model
admin.site.register(Task)