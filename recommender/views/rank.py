from django.http.response import HttpResponse
from django.shortcuts import render
from neo4j import GraphDatabase

def rank(request):
    context ={
        'isRank' : True,
        'title' : 'Ranking'
    }
    return render(request, 'recommender/rank/index.html', context)