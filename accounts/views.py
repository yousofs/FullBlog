from django.contrib.auth import views as auth_views, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from .forms import UserRegisterForm, UserProfileForm, UserLoginForm, PasswordResetForm, PasswordResetConfirmForm
from .models import UserProfile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('blog:all_posts')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:reset_done')
    form_class= PasswordResetForm
    email_template_name = 'accounts/password_reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/reset_confirm.html'
    form_class= PasswordResetConfirmForm
    success_url = reverse_lazy('accounts:password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class UserProfileView(DetailView):
    model = UserProfile
    fields = ('full_name', 'email', 'bio', 'phone_number')
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

class EditProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/edit_profile.html'
    success_message = 'Your post successfully edited!'
    
    def get_success_url(self):
        return reverse('accounts:edit_profile', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context

    def get_queryset(self):
        qs = super(EditProfile, self).get_queryset()
        return qs.filter(id=self.request.user.id)