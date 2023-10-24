from django.http import Http404
from django.shortcuts import render
from django.template import loader

from .models import Post


# Create your views here.

# def blog_views(request):
#     return render(request, 'blogs/base.html')


def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blogs/post/list.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Now post found ")
    return render(request, 'blogs/post/detail.html', {'post': post})
# def views(request):
# return render(request, 'blogs/base.html',)
