from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('timelines:index')

    def form_valid(self, form):
        pd = form.save(commit=False)
        pd.user = self.request.user
        pd.save()
        return super().form_valid(form)