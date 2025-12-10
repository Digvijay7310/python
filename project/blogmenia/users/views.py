from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from blog.models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form  = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request, user_id=None):
    if user_id:
        user_profile = CustomUser.objects.get(id=user_id)
    else:
        user_profile = request.user

    blogs = Blog.objects.filter(user=user_profile).order_by('-createdAt')
    return render(request, 'profile.html', {'profile_user': user_profile, 'blogs': blogs})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        if fullName:
            user.fullName = fullName
            user.save()
            return redirect('profile')
    return render(request, 'edit_profile.html', {'user': user})
