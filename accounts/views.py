from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import UserRegisterForm


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/reset_complete.html'
