import json
from django.http.response import HttpResponse
from django.shortcuts import render
from neo4j import GraphDatabase

def movie(request):
    context ={
        'isMovie' : True,
        'title' : 'Movie'
    }
    return render(request, 'recommender/movie/index.html', context)