from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home/home.html'

    