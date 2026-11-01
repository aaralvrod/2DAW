from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('completed/', views.task_list_completed, name='completed-task'),
    path('pending/', views.task_list_pending, name='pending-task'),
    path('<task_slug>/', views.task_detail, name='task-detail'),
    path('<task_slug>/edit/', views.edit_task, name='task-edit'),
    path('<task_slug>/delete/', views.delete_task, name='task-delete'),
    path('<task_slug>/toggle/', views.toggle_task, name='task-toggle'),
]
