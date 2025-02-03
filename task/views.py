from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Todo


class UserLoginView(LoginView):
    template_name = 'task/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'You are logged in!')
        return reverse_lazy('tasks')

    def logout(request):
        meaasges.success(request, 'You have logged out!')
        return redirect('login')


class RegisterPage(FormView):
    template_name = 'task/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'task/todo.html'


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)
        


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
