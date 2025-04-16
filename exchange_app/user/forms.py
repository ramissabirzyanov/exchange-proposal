from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 label='First name')
    last_name = forms.CharField(max_length=30,
                                required=True,
                                label='Last name')
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
        ]
