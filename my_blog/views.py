# from django.shortcuts import render
from django.views.generic import ListView
from my_blog.models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    
