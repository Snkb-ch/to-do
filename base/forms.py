from django.forms import ModelForm

from .models import Task, User
from django import forms
from django.contrib.auth import get_user_model


from django.contrib.auth.forms import UserCreationForm

class TaskForm(ModelForm):

        class Meta:

            model = Task

            fields = '__all__'
            widgets = {
                'Deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),



            }

            exclude = ['user', 'created']

class UserCreationForm(UserCreationForm):

        class Meta:

            model = User

            fields = ['name', 'email', 'password1', 'password2', 'username']
