from asyncio import tasks
from sre_constants import SUCCESS
from django.shortcuts import render,redirect

from .forms import TodoForms
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def add(request):
    if request.method == 'POST':
        name = request.POST.get("name",'')
        priority = request.POST.get("priority",'')
        date = request.POST.get("date",'')
        task = Task(name = name, priority = priority,date = date)
        task.save()
        return redirect('/')
    return render(request,'mytodoapp/add.html')

def index(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get("name",'')
        priority = request.POST.get("priority",'')
        date = request.POST.get("date",'')
        task = Task(name = name, priority = priority,date = date)
        task.save()
        return redirect('/')
    return render(request,'mytodoapp/index.html',{'task_list':task_list})

def delete(request,taskid):
    task = Task.objects.get(id = taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'mytodoapp/delete.html',{'task':task})

def edit(request,taskid):
    task=Task.objects.get(id=taskid)
    form = TodoForms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'mytodoapp/edit.html',{'form':form,'task':task})

#Generic or class based views

class TaskListView(ListView):
    model = Task
    template_name ='mytodoapp/index.html'
    context_object_name = 'task_list'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'mytodoapp/detail.html'
    context_object_name = 'task'

class TaskupdateView(UpdateView):
    model = Task
    template_name = 'mytodoapp/update.html'
    context_object_name = 'task'
    fields = {'name','priority','date'}

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'mytodoapp/delete.html'
    success_url = reverse_lazy('cbv_index')
