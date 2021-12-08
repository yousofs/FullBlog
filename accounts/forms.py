from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

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
