from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task',] 


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'