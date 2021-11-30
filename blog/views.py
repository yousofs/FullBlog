from django.shortcuts import render
from .models import Posts


def AllPosts(request):
    posts = Posts.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': posts})


def PostDetail(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
