from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin

from accounts.models import UserProfile
from .models import Post, Comment, Tag
from .forms import BlogCommentForm, AddPostForm, EditPostForm


class AllPostView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    paginate_by = 2
    paginate_orphans = 1
    ordering = ["-created"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context


class PostDetailView(DetailView, FormMixin):  # Post_detail & Comment together!
    model = Post
    form_class = BlogCommentForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            comment = Comment(
                post=self.object, user=self.request.user, body=form.cleaned_data["body"]
            )
            comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy("blog:all_posts")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request, "You post has successfully submitted!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context


class EditPostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog/edit_post.html"
    success_message = "Your post successfully edited!"

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:all_posts")
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context


class TagDetailView(DetailView):
    model = Post
    template_name = "blog/tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.get(tag=self.kwargs["slug"])
        context["profile"] = UserProfile.objects.filter(id=self.request.user.id).first()
        return context
