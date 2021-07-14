from django import forms
from django.contrib.auth.forms import UserCreationForm


class Login(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your @username'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class Register(UserCreationForm):
    # username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your @username'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your emial'}))
    # password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    # confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))
    pass

