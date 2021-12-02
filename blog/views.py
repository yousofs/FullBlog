from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Post


class AllPostView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    paginate_by = 5
    ordering = ['-created']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog:all_posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request, 'You post has successfully submitted!')
        return super().form_valid(form)


class EditPostView(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog:all_posts')
    success_message = 'Your post successfully edited!'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_posts')
    success_message = "Thing was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)
