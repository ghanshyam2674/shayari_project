from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput())
    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'username','email' ]
        fields = ['username','email' ]

        labels = { 'email': 'Email', }
    