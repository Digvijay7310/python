from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.blog_create, name='create_blog'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('<int:id>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:id>/delete/', views.blog_delete, name="blog_delete"),
]
