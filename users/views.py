from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from .utils import DataMixin


class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):

    form_class = LoginUserForm
    template_name = 'users/login.html'
    error_message = "Something went wrong"
    success_url = reverse_lazy("home")
    user = ""
    # next_page = '/'
    # next = 'home'
    success_message = f"Successfully login"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        print(context)
        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(LogoutView, SuccessMessageMixin):

    next_page = "home"
    success_message = "Logout successfully"
