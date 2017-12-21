from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect('login')


# #


# class LogoutView(LogoutView):
#     success_url = reverse_lazy('base.html')

# def form_valid(self, form):
#     form.save()
#     return redirect('logout')


def logout_view(request):
    logout(request)
    return redirect('base.html')


from django.contrib.auth import logout

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
