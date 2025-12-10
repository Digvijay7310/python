from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view , name="login_view"),
    path('profile/', views.profile_view , name="profile_view"), 
    path('profile/<int:user_id>/', views.profile_view , name="profile_other"),  
    path('edit-profile/', views.edit_profile , name="edit_profile"),
    path('logout/', views.logout_view , name="logout"),
    path('register/', views.register_view , name="register_view"),
]
