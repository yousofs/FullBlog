from django import forms
from .models import Comment, Post


class BlogCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='')
    def __init__(self, *args, **kwargs):
        super(BlogCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs = {
            'rows': '3',
            'class': 'form-control',
            'placeholder': 'Join the discussion and leave a comment!',
        }
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'id': 'title',
        }
        self.fields['tag'].widget.attrs = {
            'class': 'form-select',
            'id': 'tag',
        }
        self.fields['img'].widget.attrs = {
            'class': 'form-control',
            'type': 'file',
            'id': 'image',
        }
        self.fields['description'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'id': 'description',
        }
        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'id': 'body',
            'rows': '5'
        }

    class Meta:
        model = Post
        fields = ('title', 'tag', 'img', 'description', 'body')


class EditPostForm(forms.ModelForm):
    img = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'id': 'title',
        }
        self.fields['tag'].widget.attrs = {
            'class': 'form-select',
            'id': 'tag',
        }
        self.fields['img'].widget.attrs = {
            'class': 'form-control',
            'type': 'file',
            'id': 'image',
        }
        self.fields['description'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'id': 'description',
        }
        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'id': 'body',
            'rows': '5'
        }
        
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'img', 'description')