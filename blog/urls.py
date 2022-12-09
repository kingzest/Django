from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.BlogPage.as_view(), name='blog_page'),
    path('<slug:slug>/', views.PostPage.as_view(), name='post_page'),
]