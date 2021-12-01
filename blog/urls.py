from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPostView.as_view(), name='all_posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
]
