from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", 'first_name', 'last_name', "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # self.fields['last_name'].required = True


    def clean(self):
        cleaned_data = super().clean()
    #     email = cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("This email address is already in use.")
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email):
            raise forms.ValidationError("This email address is already in use.")
        return email