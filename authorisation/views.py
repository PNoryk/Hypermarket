from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, FormView
from django.shortcuts import redirect

from authorisation.forms import MyRegistrationForm, MyLoginForm


class MyRegistrationView(FormView):
    form_class = MyRegistrationForm
    template_name = 'myAuth/registration.html'

    # success_url = 'login'

    def form_valid(self, form):
        form.save()
        # self.register(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')


class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = 'myAuth/login.html'

    # def get_success_url(self):
    #     return super().get_success_url()

    # def form_valid(self, form):
        # user = form.get_user()
        # if user.is_staff:
        #     self.success_url = r"/admin"
        #     login(self.request, user)
        #     return redirect("/admin")

        # return super(MyLoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('home')
