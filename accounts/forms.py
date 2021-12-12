from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, AuthenticationForm, PasswordResetForm
from django.contrib.auth import views as auth_views
from .models import UserProfile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'email', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'id': 'password', 'type': 'password'}
))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control form-control-lg',
            'id': 'full_name',
        }
        self.fields['phone_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control form-control-lg',
            'id': 'phone',
        }
        self.fields['email'].widget.attrs = {
            'type': 'email',
            'class': 'form-control form-control-lg',
            'id': 'email',
        }
        self.fields['password1'].widget.attrs = {
            'type': 'password',
            'class': 'form-control form-control-lg',
            'id': 'password1',
        }
        self.fields['password2'].widget.attrs = {
            'type': 'password',
            'class': 'form-control form-control-lg',
            'id': 'password2',
        }
    class Meta:
        model = UserProfile
        fields = ('email', 'full_name', 'phone_number')


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('email', 'full_name')

    def clean_password2(self):
        cd = self.changed_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password must match')

        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password = self.changed_data['password2']
        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'full_name')

    def clean_password(self):
        return self.intial['password']


class UserProfileForm(forms.ModelForm):
    img = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'type': 'email',
        }
        self.fields['phone_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
        }
        self.fields['bio'].widget.attrs = {
            'class': 'form-control',
            'rows': '5'
        }
        self.fields['img'].widget.attrs = {
            'class': 'form-control',
            'type': 'file',
        }
    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'bio', 'phone_number', 'img')

class PasswordResetForm(auth_views.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'type': 'email'}))
    
class PasswordResetConfirmForm(auth_views.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetConfirmForm, self).__init__(*args, **kwargs)
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'old_password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'new_password1'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'new_password2'}))
    