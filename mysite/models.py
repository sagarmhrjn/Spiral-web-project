from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import Truncator
from markdown import markdown
from django.utils.html import mark_safe


class Info(models.Model):
    title = models.CharField(max_length=350, blank=True)
    message =  models.TextField(blank=True)
    image = models.ImageField(upload_to="mysite_img",blank=True)


    def __str__(self):
        return self.title

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)


    def save(self, **kwargs):
        # run the save method of our parent class
        super().save()
        # (image) imported from pillow library
        img = Image.open(self.image.path)

        if img is not None:
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
