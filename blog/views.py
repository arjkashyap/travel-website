from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk = pk) 
    return render(request, 'blog/post.html', {'post': post})

