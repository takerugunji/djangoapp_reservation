from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def about(request):
    return render(request, 'posts/about.html')
    

def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def blog(request):
    posts = Post.objects.order_by('-published')
    page_obj = paginate_queryset(request, posts, 6)
    return render(request, 'posts/blog.html', {'posts': posts, 'page_obj': page_obj})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
