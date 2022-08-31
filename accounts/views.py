from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
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