from django.urls import path
from .views import PostListAPIView
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('api/posts/', PostListAPIView.as_view()), 
]