from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'detail'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    context_object_name = 'news_create'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'news_edit'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
