from django.shortcuts import render
from .models import Info
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from boards.models import Board

# Create your views here.
def home(request):
    ctx = Info.objects.all().first()
    posts =Post.objects.all().first()
    boards = Board.objects.all()
    data = {
        'ctx': ctx,
        'posts': posts,
        'boards': boards
    }
    return render(request, 'mysite/home.html', data, {'title': 'Home'})


def about(request):
    ctx = Info.objects.get(id=1)
    return render(request, 'mysite/about.html', {'ctx': ctx,'title': 'About'})


def contact(request):
    ctx = Info.objects.get(id=2)
    return render(request, 'mysite/contact.html', {'ctx': ctx, 'title': 'Contact'})
