from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task

class TaskForm(forms.ModelForm):
   class Meta:
      model=Task
      fields=["title","description"]
   
   
   

# Create your views here.
def index(request):
   return render(request,'todoapp/index.html',{
      "tasks": Task.objects.all()
   })
def addTask(request):
   if(request.method=="POST"):
      form=TaskForm(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         description=form.cleaned_data["description"]
         newTask=Task(title=title,description=description)
         newTask.save()
         return HttpResponseRedirect(reverse("todoapp:index"))
      else:
         return render(request,'todoapp/addTask.html',{
            "form": form
         })
   else:
      return render(request,'todoapp/addTask.html',{
         "form": TaskForm()
      })
def taskDetail(request,task_id):
   task=Task.objects.get(pk=task_id)
   return render(request,'todoapp/taskDetail.html',{
      "task": task
   })
def deleteTask(request,task_id):
   task=Task.objects.get(pk=task_id)
   task.delete()
   return HttpResponseRedirect(reverse("todoapp:index"))
def updateTask(request,task_id):
   task=Task.objects.get(pk=task_id)
   if(request.method=="POST"):
      form=TaskForm(request.POST,instance=task)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse("todoapp:index"))
      else:
         return render(request,'todoapp/updateTask.html',{
            "form":form,
            "task":task
         })
   else:
      form=TaskForm(instance=task)
      return render(request,'todoapp/updateTask.html',{
         "form":form,
         "task":task
      })