from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request, post_id):
    latest_post = Post.objects.order_by('-pub_date')
    for post in latest_post:
        if post.id == post_id:
            Title = post.id
            Content = post.content
            Date = post.pub_date
            return HttpResponse(f'{Title}\n{Date}\n\n{Content}')
        else:
            return HttpResponse('Post Does Not Exist')