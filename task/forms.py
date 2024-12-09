from django import forms
from django.forms import ModelForm
from .models import *

class TodoForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add in a new task'}))

    class Meta:
        model = todo
        fields = '__all__'