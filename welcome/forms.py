from django import forms
from django.contrib.auth.models import User


choices_user = (("1", "Student"),
                ("2", "Teacher"))

class UserForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())


class UserType(forms.Form):
    user_choice = forms.ChoiceField(choices = choices_user)
