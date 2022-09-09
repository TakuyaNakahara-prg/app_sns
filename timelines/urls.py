from django.urls import path
from . import views

app_name = 'timelines'

urlpatterns = [
    path('top/', views.TopView.as_view(), name = 'top'),
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('create/', views.PostCreateView.as_view(), name = 'create'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name = 'delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name = 'update'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name = 'comment'),
    path('userpost/<int:user>/', views.UserPostView.as_view(), name = 'userpost'),
]
