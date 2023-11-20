
from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class A(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_sent.html'
    
class B(auth_views.PasswordResetView):
    template_name='password.html'
    success_url = reverse_lazy('accounts:password_reset_done')
        