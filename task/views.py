from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo

class UserLoginView(LoginView):
    template_name = 'task/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

def get_success_url(self):
    return reverse_lazy('tasks')


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'tasks'


class TodoDetail(LoginRequiredMixin, DetailView):
     model = Todo   
     context_object_name = 'task'
     template_name = 'task/todo.html'


class TodoCreate(LoginRequiredMixin, CreateView):
     model = Todo
     fields = '__all__'
     success_url = reverse_lazy('tasks')

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
