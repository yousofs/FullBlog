from django import forms
from .models import Comment, Tag, Post


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
