from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView

from posts.models import Post, Comments


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, HitCountDetailView):
    model = Post
    template_name = 'posts/detail.html'
    count_hit = True


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ('title', 'summary', 'content', 'photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('title', 'summary', 'content', 'photo')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts_list')


class CommentCreateView(CreateView):
    model = Comments
    template_name = 'posts/create_comment.html'
    fields = ('content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comments
    template_name = 'posts/update_comment.html'
    fields = ('content',)

class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'posts/delete_comment.html'
    success_url = reverse_lazy('posts_list')
