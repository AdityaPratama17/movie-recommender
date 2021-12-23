from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'isDashboard' : 'dashboard'
    }
    return render(request, 'recommender/index.html',context)

def recommender(request):
    context ={
        'isRecommender' : 'recommender'
    }
    return render(request, 'recommender/recommender/index.html',context)

def result(request,id):
    context ={
        'isRecommender' : 'recommender'
    }
    return render(request, 'recommender/recommender/result.html',context)

def user(request):
    context ={
        'isUser' : 'masterdata'
    }
    return render(request, 'recommender/user/index.html', context)

def movie(request):
    context ={
        'isMovie' : 'masterdata'
    }
    return render(request, 'recommender/movie/index.html', context)

def link(request):
    context ={
        'isLink' : 'masterdata'
    }
    return render(request, 'recommender/link/index.html', context)