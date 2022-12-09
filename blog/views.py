from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
# Create your views here.


class BlogPage(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-pub_date')
    template_name = 'blog/index.html'
    context_object_name = 'blog_page'


class PostPage(generic.DetailView):
    model = Post
    template_name = 'blog/post-template.html'
    context_object_name = 'post_page'