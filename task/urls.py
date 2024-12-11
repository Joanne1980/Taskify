from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('', TodoList.as_view(), name="tasks"),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='task'),
    path('create-todo/', TodoCreate.as_view(), name="task-create"),

]