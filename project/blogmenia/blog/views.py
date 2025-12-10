from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def blog_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        category = request.POST['category']

        Blog.objects.create(
            user = request.user,
            title=title,
            content=content,
            image=image,
            category=category
        )
        return redirect('home')
    
    return render(request, 'create_blog.html', {'categories': Blog.CATEGORY_CHOICES})

def home(request):
    blogs = Blog.objects.all().order_by('-createdAt')
    return render(request, 'home.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_search(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    blogs = Blog.objects.all()

    if query:
        blogs = blogs.filter(title__icontains=query)

    if category and category != 'all':
        blogs = blogs.filter(category=category)

    return render(request, 'blog_search.html', {
        'blogs': blogs,
        'categories': Blog.CATEGORY_CHOICES,
        'selected_category': category,
        'search_query': query,
    })

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
