from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


# Create your views here.

# def blog_views(request):
#     return render(request, 'blogs/base.html')


# def post_list(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     print(post_list)
#     return render(request, 'blogs/post/list.html', {'posts': posts})

class PostListView(ListView):
    """Alternative Post View """
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 4
    template_name = "blogs/post/list.html"


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Now post found ")
    return render(request, 'blogs/post/detail.html', {'post': post})


# def views(request):
# return render(request, 'blogs/base.html',)

# def post_share(request, id):
#     print('1')
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#     sent = False
#     print('2')
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         print('3')
#         if form.is_valid():
#             cd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"{cd['name']} recommended you read {post.title}"
#             message = f"read {post.title} at {post_url}\n\n {cd['name']} \'s comments: {cd['comments']}"
#             send_mail(subject, message, 'abhishekvadhera34@gmail.com', [cd['to']])
#             sent = True
#     else:
#         form = EmailPostForm()
#     return render(request, 'blogs/post/share.html', {'post': post, 'form': form, 'sent': sent})


from django.shortcuts import render, get_object_or_404


def post_share(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommended you read {post.title}"
            message = f"read {post.title} at {post_url}\n\n {cd['name']} \'s comments: {cd['comments']}"
            send_mail(subject, message, 'abhishekvadhera34@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blogs/post/share.html', {'post': post, 'form': form, 'sent': sent, 'post_id': id})
