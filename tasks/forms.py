from socket import fromshare
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import task

class Registeruser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']



class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important']
