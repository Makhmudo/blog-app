from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'detail'

