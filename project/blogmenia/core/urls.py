"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import register_view, login_view, logout_view, profile_view, edit_profile
from blog.views import home, blog_create, blog_detail, blog_edit, blog_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name="profile"),
    path('profile/<int:user_id>/', profile_view, name='profile_other'),
    path('profile/edit/', edit_profile, name="edit_profile"),

    path('blog/create/', blog_create, name='create_blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('blog/<int:id>/edit/', blog_edit, name='blog_edit'),
    path('blog/<int:id>/delete/', blog_delete, name="blog_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
