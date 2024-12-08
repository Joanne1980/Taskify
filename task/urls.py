from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('update/<str:pk>/', views.update, name="update"),
]