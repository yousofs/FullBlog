from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Post, Comment
from .forms import BlogCommentForm


class AllPostView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    paginate_by = 5
    ordering = ['-created']


class PostDetailView(DetailView, FormMixin):  # Post_detail & Comment together!
    model = Post
    form_class = BlogCommentForm
    template_name = 'blog/post_detail.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            comment = Comment(post=self.object, user=self.request.user, body=form.cleaned_data['body'])
            comment.save()
        return super().form_valid(form)


class AddPostView(CreateView):
    model = Post
    fields = ('title', 'body', 'tag')
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
    fields = ('title', 'body', 'tag')
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog:all_posts')
    success_message = 'Your post successfully edited!'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_posts')
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)
