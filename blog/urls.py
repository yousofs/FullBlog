from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPosts, name='all_posts'),
    path('post/<int:post_id>/', views.PostDetail, name='post'),
]
