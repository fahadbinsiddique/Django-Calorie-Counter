from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from calorie_app.models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields.values():
            f.widget.attrs.update({"class": "form-control"})


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields.values():
            f.widget.attrs.update({"class": "form-control"})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
        exclude = ["user", "bmr"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields.values():
            f.widget.attrs.update({"class": "form-control"})


class CalorieConsumeForm(forms.ModelForm):
    class Meta:
        model = CalorieConsumeModel
        fields = ["item_name", "calorie_consume"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields.values():
            f.widget.attrs.update({"class": "form-control"})
