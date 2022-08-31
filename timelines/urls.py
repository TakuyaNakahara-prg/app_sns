from django.urls import path
from . import views

app_name = 'timelines'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('create/', views.PostCreateView.as_view(), name = 'create'),
]