from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    posts = Blog.objects
    return render(request, "blog/home.html", {'posts' : posts})
def detail(request, id_post):
    post = get_object_or_404(Blog, pk=id_post)
    return render(request, "blog/detail.html", {"post" : post})