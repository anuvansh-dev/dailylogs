from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .models import BackgroundImage
from .forms import TaskForm
from .forms import BackgroundImageForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here. 

# User Authentication
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = UserCreationForm()
            
    return render(request, 'register.html', {'form': form})
        
        
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            next_url = request.GET.get('next', 'task_list')  # Default to task_list if no next parameter
            return redirect(next_url)  
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# Task Management
@login_required
def task_list(request):
    tasks = Tasks.objects.filter(user=request.user)
    # handle toggle switch 
    if request.method == "POST" and "toggle_completed" in request.POST:
        task_id = request.POST.get('task_id') # get the task id from the form
        task = Tasks.objects.get(id=task_id)    # fetch the task from the model using 'id'
        task.is_completed = not task.is_completed # toggle the completion status
        task.save() # save the updated status
        return redirect('task_list')
    
    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'add_task.html', {'form': form})
    
    
def task_detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)
    return render(request, 'task_detail.html', {'task': task})


def task_edit(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_edit.html', {'form': form})


def task_delete(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)
    
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
    return render(request, 'task_delete.html', {'task': task})


def upload_background(request):
    background = BackgroundImage.objects.first()
    
    if request.method == "POST":
        form = BackgroundImageForm(request.POST, request.FILES, instance=background)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = BackgroundImageForm(instance=background)
        
    return render(request, 'upload_background.html', {'form': form})