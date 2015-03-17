from django.shortcuts import render, get_object_or_404

from .models import Post

def posts(request):
    post_list = Post.objects.filter(is_published=True)
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts.html', context)

def detail(request):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
