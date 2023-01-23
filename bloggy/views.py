from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, "bloggy/blog.html", context)

def category(request):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'category':category
    }
    return render(request, "bloggy/category.html", context)
    