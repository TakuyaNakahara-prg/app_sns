from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User
from timelines.models import Post
# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_done')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignupDoneView(TemplateView):
    template_name = 'signup_done.html'


