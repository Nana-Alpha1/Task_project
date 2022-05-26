from django.db import models

# Create your models here.

class TaskModel(models.Model):
    task = models.CharField(max_length=100)
    isComplete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.task