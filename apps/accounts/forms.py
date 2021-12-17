from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import UserModel


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = UserModel
        fields = ['email', 'username', 'first_name', 'last_name',
                  'password1', 'password2', 'company', 'department']