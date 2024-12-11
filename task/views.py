from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import TodoForm


# Create your views here.
def todo_view(request):
    form = TodoForm()
    task = None  # Define or fetch your task here if needed

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"task": task, "form": form}
    return render(request, "task/todo.html", context)  # Replace with your actual template


def update(request, pk):
    task = Todo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "task/update.html", context)


def delete(request, pk):
    task = get_object_or_404(Todo, id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {"item": item}
    return render(request, "task/delete.html", context)
