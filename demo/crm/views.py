from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

def homepage(request):
    return render(request, 'crm/index.html')

def tasks(request):
    
    queryDataAll = Task.objects.all()
    context = {'AllTask': queryDataAll}
    
    return render(request, 'crm/view-tasks.html',context)

def register(request):
    return render(request,'crm/register.html')

def create_task(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('view-tasks')
     
    context = {'TaskForm':form}
    
    return render(request, 'crm/create-task.html',context)
