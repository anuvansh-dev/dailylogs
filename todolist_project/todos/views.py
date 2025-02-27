from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForm


# Create your views here. 

def task_list(request):
    tasks = Tasks.objects.all()
    # handle toggle switch 
    if request.method == "POST" and "toggle_completed" in request.POST:
        task_id = request.POST.get('task_id') # get the task id from the form
        task = Tasks.objects.get(id=task_id)    # fetch the task from the model using 'id'
        task.is_completed = not task.is_completed # toggle the completion status
        task.save() # save the updated status
    
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})
    
    
def task_detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_edit(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
    return render(request, 'task_delete.html', {'task': task})