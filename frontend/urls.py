from django.urls import include, path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('stone/', views.stone, name='stone'),
    path('<str:name>/<int:Age>/<str:Skill>', views.index, name='index'),
]