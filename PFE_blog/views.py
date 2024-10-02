from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    
class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']
    success_url = '/'