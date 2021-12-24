from django.http.response import HttpResponse
from django.shortcuts import render
from neo4j import GraphDatabase

def tag(request):
    context ={
        'isTag' : True,
        'title':'Tag'
    }
    return render(request, 'recommender/tag/index.html', context)