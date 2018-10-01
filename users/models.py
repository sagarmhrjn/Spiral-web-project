from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='image_default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # override the save method, this save method is the method that gets run after our model is saved.
     # it's a method that already exist in our parent class but we're creating our own so that we can add some functionality


# Signature of the base method in class Model is save(self, **kwargs) and method overriding it should have the same signature,
# so add **kwargs as an argument to save makes sense.﻿
    def save(self, **kwargs):
        # run the save method of our parent class
        super().save()
        # (image) imported from pillow library
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
