from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'registration/profile.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'registration/update.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'country']
    success_url = reverse_lazy("home")


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('home')
