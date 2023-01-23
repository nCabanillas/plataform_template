from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

def store(request):
    return render(request, "blog/store.html")
