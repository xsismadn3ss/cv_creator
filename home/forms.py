from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        help_texts = {
            'username': ""
        }
        labels = {
            'username': 'Nombre de usuario',
            'first_name': "Nombres",
            'last_name': "Apellidos",
            'email': 'Email'
        }
