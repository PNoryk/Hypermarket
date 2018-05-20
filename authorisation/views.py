from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *


class MyRegistrationView(FormView):
    form_class = MyRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        # self.register(form)
        return redirect('login')


class MyLoginView(LoginView):
    form_class = MyLoginForm

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        user = form.get_user()
        if user.is_staff:
            self.success_url = r"/admin"
            login(self.request, user)
            return redirect("/admin")

        return super(MyLoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('base.html')
