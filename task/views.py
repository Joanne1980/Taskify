from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteTodo(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
