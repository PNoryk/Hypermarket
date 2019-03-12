from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-registrationForm"
        self.helper.form_class = 'registerForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'home'
        self.helper.layout = Layout(
            Field('username', css_class='input-xlarge'),
            Field('password1', css_class='input-xlarge'),
            Field("password2", css_class='input-xlarge'),
            FormActions(
                Submit('register', 'Register', css_class="btn-primary"),
            ))


class MyLoginForm(AuthenticationForm):
    pass


class MuLogoutForm(UserChangeForm):
    pass
