from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.
def index(request):
    task = todo.objects.all()

    form = TodoForm()

    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task':task, 'form':form}
    return render(request, 'task/todo.html', context)

def update(request, pk):
    task = todo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == 'POST': 
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'task/update.html', context) 

def delete(request, pk):
        item = todo.objects.get(id=pk)

        if request.method == 'POST': 
            item.delete()
            return redirect('/')

        context = {'item':item}
        return render(request, 'task/delete.html', context)   