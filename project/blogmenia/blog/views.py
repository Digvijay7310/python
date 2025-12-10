from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def blog_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']

        Blog.objects.create(
            user = request.user,
            title=title,
            content=content,
            image=image
        )
        return redirect('home')
    
    return render(request, 'create_blog.html')

def home(request):
    blogs = Blog.objects.all().order_by('-createdAt')
    return render(request, 'home.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})


@login_required
def blog_edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.user != request.user:
        return redirect('home')  # can't edit others blog

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        if request.FILES.get('image'):
            blog.image = request.FILES.get('image')
        blog.save()
        return redirect('profile')
    
    return render(request, 'edit_blog.html', {'blog': blog})

@login_required
def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.user == request.user:
        blog.delete()
    return redirect('profile')
