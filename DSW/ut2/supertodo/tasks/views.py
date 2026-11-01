from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Todas las tareas'})


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/task/add.html', {'form': form, 'subtitle': 'Añadir tarea'})


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/detail.html', {'task': task})


def task_list_pending(request):
    tasks = Task.objects.filter(completed=False)
    return render(
        request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Tareas pendientes'}
    )


def task_list_completed(request):
    tasks = Task.objects.filter(completed=True)
    return render(
        request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Tareas completadas'}
    )


def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.delete()
    return redirect('tasks:task-list')


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)

    return render(
        request, 'tasks/task/edit.html', {'task': task, 'form': form, 'subtitle': 'Editar tarea'}
    )


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task-list')
