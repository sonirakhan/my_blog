from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status="PUBLISHED")
    paginator = Paginator(posts,2)          # 2 post per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,template_name='blog/post_list.html',context={'page_obj': page_obj})


def post_detail(request, post_slug):
    posts = get_object_or_404(Post,slug=post_slug,status='PUBLISHED')
    return render(request,template_name='blog/post_detail.html',context={'posts':posts})


