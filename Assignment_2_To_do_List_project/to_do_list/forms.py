from django import forms
from to_do_list.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']