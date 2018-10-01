from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from markdown import markdown
from django.utils.html import mark_safe


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # find the location to specific post
    def get_absolute_url(self):
        # reverse will simply return URL  as a string and let view handle the redirect for us
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
