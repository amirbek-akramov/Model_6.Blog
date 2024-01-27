from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('title', 'summary', 'content', 'photo')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
