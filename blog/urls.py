from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPostView.as_view(), name='all_posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/add_post/', views.AddPostView.as_view(), name='add_post'),
    path('post/edit_post/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),
    path('post/delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
]
