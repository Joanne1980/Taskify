from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, DeleteTodo, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TodoList.as_view(), name="tasks"),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='task'),
    path('create-todo/', TodoCreate.as_view(), name="task-create"),
    path('update-todo/<int:pk>/', TodoUpdate.as_view(), name='task-update'),
    path('delete-todo/<int:pk>/', DeleteTodo.as_view(), name='task-delete'),

]
