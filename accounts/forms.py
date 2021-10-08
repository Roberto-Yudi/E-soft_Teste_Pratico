from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label=("Senha"),)
    password2 = forms.CharField(label=("Confirme a senha"),)
    class Meta:
        model = CustomUser
        fields = ('email', 'idade', 'nascimento', 'apelido', 'observação')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'