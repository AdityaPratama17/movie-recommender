import json
from django.http.response import HttpResponse
from django.shortcuts import render
from neo4j import GraphDatabase


# Create your views here.
def index(request):
    context ={
        'isRecommendation' : True,
        'title':'Recommendation'
    }
    return render(request, 'recommender/index.html',context)

def result(request, id):
    context ={
        'isRecommendation' : True,
        'title':'Result'
    }
    return render(request, 'recommender/result.html',context)
    
def movie(request):
    context ={
        'isMovie' : True,
        'title' : 'Movie'
    }
    return render(request, 'recommender/movie/index.html', context)

def tag(request):
    context ={
        'isTag' : True,
        'title':'Tag'
    }
    return render(request, 'recommender/tag/index.html', context)

def rank(request):
    context ={
        'isRank' : True,
        'title' : 'Ranking'
    }
    return render(request, 'recommender/rank/index.html', context)