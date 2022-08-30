from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models

# Create your views here.

def list_todo_items(request):
    context = {'todos': models.Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request):
    content = request.POST.get('content')
    todo = models.Todo(content = content)
    todo.save()
    return redirect('/todos/list')

def delete_todo_item(request, id):
    todo = models.Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/list/')