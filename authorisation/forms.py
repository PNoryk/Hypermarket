from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .validators import *


class MyRegistrationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]

        lv = LoginValidation(username)
        lv.check_username()

        return username

    def clean_password2(self):
        password = self.cleaned_data["password1"]

        pv = PasswordValidation(password)
        pv.check_pass()

        return password


class MyLoginForm(AuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]

        lv = LoginValidation(username)
        lv.check_username()

        return username

    def clean_password(self):
        password = self.cleaned_data["password"]

        pv = PasswordValidation(password)
        pv.check_pass()

        return password


class MuLogoutForm(UserChangeForm):
    pass
