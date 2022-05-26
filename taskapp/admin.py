from atexit import register
from django.contrib import admin
from . models import TaskModel

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display=('task','date','isComplete')

admin.site.register(TaskModel,TaskModelAdmin)