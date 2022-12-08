from django.urls import include, path
from . import views


urlpatterns = [
    path('id=<int:post_id>', views.index, name='index'),
]