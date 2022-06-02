from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(req):
    tasks = Task.objects.order_by('title')
    return render(req, 'main/index.html', {
        'title': 'Main page',
        'tasks': tasks,
    })


def about(req):
    return render(req, 'main/about.html')


def create(req):
    error = ''
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is invalid'
    form = TaskForm()
    ctx = {
        'form': form,
        'error': error
    }
    return render(req, 'main/create.html', ctx)

def delete(req):
    #delete element onclick
    if req.method == 'POST':
        title = req.POST.get('title')
        task = Task.objects.get(title = title)
        task.delete()
        return redirect('delete')
    else:
        tasks = Task.objects.order_by('title')
        return render(req, 'main/delete.html', {
            'title': 'Delete page',
            'tasks': tasks,
        })