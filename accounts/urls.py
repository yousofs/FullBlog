from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
    path('reset_done/', views.PasswordResetDone.as_view(), name='reset_done'),
    path('reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]
