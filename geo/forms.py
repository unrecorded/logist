from django import forms
from geo.models import Geo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Geo
        fields = "__all__"

#Форма авторизации
class LoginForm(AuthenticationForm):

    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Логин', 
                               'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control',
        'data-toggle': 'password',
        'id': 'password',
        'name': 'password',
        }))
    remember_me = forms.BooleanField(required=False)

    class Meta:

        model = User
        fields = ['username', 'password', 'remember_me']
