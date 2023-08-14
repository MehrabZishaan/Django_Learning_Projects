from django.shortcuts import render, redirect
from to_do_list.models import TaskModel
from to_do_list.forms import TaskForm
from django.views.generic import View, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

class HomeView(TemplateView):
    template_name = 'home.html'


# def add_task(request):
#     return render(request, 'add_task.html')

class AddTaskView(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')
    
# def show_tasks(request):
#     tasks = TaskModel.objects.all()
#     return render(request, 'show_tasks.html', {'tasks': tasks})

class ShowTaskView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)
    
class EditTaskView(UpdateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')
    
class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_tasks')
    
class CompletedTaskView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)
    
class CompleteTaskView(View):
    def get(self, request, task_id):
        task = TaskModel.objects.get(pk=task_id)
        task.is_completed = True
        task.save()
        return redirect('completed_tasks')