from django.db import models
from django.utils.text import slugify
from accounts.models import UserProfile


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.title[:20]}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
