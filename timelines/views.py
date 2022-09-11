from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from accounts.models import User
# Create your views here.
class TopView(TemplateView):
    template_name = 'top.html'

@method_decorator(login_required, name = 'dispatch')
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        return queryset
    

@method_decorator(login_required, name = 'dispatch')
class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

@method_decorator(login_required, name = 'dispatch')
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
    

@method_decorator(login_required, name = 'dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('timelines:index')

    def delete(self,request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

@method_decorator(login_required, name = 'dispatch')
class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'update.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('timelines:index')

@method_decorator(login_required, name = 'dispatch')
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment.html'
    form_class = CommentCreateForm
    success_url = reverse_lazy('timelines:detail')

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post  
        comment.user = self.request.user
        comment.save()
        return redirect('timelines:detail', pk=post.pk)

class UserPostView(ListView):
    template_name = 'userpost.html'

    def get_queryset(self):
        user_id = self.kwargs['user']
        queryset = Post.objects.filter(user = user_id)
        return queryset
    


