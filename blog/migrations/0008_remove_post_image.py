# Generated by Django 2.1.1 on 2018-09-30 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]