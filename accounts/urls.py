from django.urls import path
from .views import SignUpView, ProfileView, ProfileDeleteView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update')
]
