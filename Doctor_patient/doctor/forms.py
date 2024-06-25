# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'user_type')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'user_type')
