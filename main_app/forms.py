from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='user name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())