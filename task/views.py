from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Todo
# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'


class TodoDetail(DetailView):
     model = Todo   
     context_object_name = 'task'
     template_name = 'task/todo.html'

class TodoCreate(CreateView):
     model = Todo
     fields = '__all__'
     success_url = reverse_lazy('tasks')









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
