from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, name, Age, Skill):
    return render(request, 'frontend/index.html', context={'name':name,'Age':Age,'Skill':Skill, 'athlete_list':['precious', 'Obaloluwa', 'Ibrahim']})


def stone(request):
    return HttpResponse('Who is Stone?')