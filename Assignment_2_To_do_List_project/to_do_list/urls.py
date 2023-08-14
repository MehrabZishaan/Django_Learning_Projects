from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='homepage'),
    path('', views.HomeView.as_view(template_name='home.html'), name='homepage'),
    # path('add_task/', views.add_task, name='add_task'),
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
    # path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('show_tasks/', views.ShowTaskView.as_view(), name='show_tasks'),
    path('edit_task/<int:pk>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
    # path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('completed_tasks/', views.CompletedTaskView.as_view(), name='completed_tasks'),
    path('complete/<int:task_id>/', views.CompleteTaskView.as_view(), name='complete_task'),
    
]