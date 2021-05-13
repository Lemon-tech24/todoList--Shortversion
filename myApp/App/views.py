from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList


# Create your views here.

def index(request):
    form = ToDoList.objects.all()
    return render(request, 'index.html', {'form': form})

def AddItem(request):
    new_item = ToDoList(name=request.POST['content'])
    new_item.save()
    return redirect('/')

def DeleteItem(request, todo_id):
    delete_item = ToDoList.objects.get(id=todo_id)
    delete_item.delete()
    return redirect('/')

