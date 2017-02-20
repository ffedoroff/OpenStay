from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class HostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address', 'city', 'country']
