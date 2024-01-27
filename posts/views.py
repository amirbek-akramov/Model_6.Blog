from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView

from posts.models import Post


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'


class PostDetailView(LoginRequiredMixin, HitCountDetailView):
    model = Post
    template_name = 'posts/detail.html'
    # context_object_name = 'post'
    count_hit = True


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ('title', 'summary', 'content', 'photo')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('title', 'summary', 'content', 'photo')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts_list')

