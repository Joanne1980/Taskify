from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.
def index(request):
    task = todo.objects.all()

    form = Todoform()

    if request.method =='POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task':task, 'form':form}
    return render(request, 'task/todo.html', context)