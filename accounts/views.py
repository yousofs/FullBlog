from django.contrib.auth import views as auth_views, login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from accounts.forms import UserRegisterForm
from .models import UserProfile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('blog:all_posts')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


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


class ProfileView(ListView):
    model = UserProfile
    template_name = 'accounts/profile.html'


class EditProfile(SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = ('full_name', 'email', 'bio', 'phone_number')
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Your post successfully edited!'
