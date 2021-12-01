from django.views.generic import DetailView, ListView

from .models import Posts


class AllPostView(ListView):
    model = Posts
    template_name = 'blog/all_posts.html'
    paginate_by = 5
    ordering = ['-created']


class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'
