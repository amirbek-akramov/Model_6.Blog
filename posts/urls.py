from django.urls import path
from .views import (
    PostsListView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    PostDetailView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView
    )

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('post/<int:pk>/comment/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comment/update/', CommentUpdateView.as_view(), name='comment_update')
]