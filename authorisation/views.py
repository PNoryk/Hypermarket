from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *


class RegisterView(LoginView):
    form_class = MyRegForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect('login')


class MyLoginView(LoginView):
    form_class = MyLoginForm


def logout_view(request):
    logout(request)
    return redirect('base.html')
