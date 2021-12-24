import json
from django.shortcuts import render
from neo4j import GraphDatabase

def rank(request):
    graphdb = GraphDatabase.driver(uri="bolt://localhost:11003", auth=("neo4j","1234"))
    # graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","1234"))
    session = graphdb.session()
    query = "MATCH(m:Movie)<-[r:givesRating]-(u:User) RETURN  m.ID AS id_movie,  m.Title AS title, AVG(r.Rating) AS avg, COUNT(u) AS tot  ORDER BY avg DESC"
    nodes = session.run(query)
    data = json.dumps(nodes.data())
    data = json.loads(data)

    context ={
        'isRank' : True,
        'title' : 'Ranking',
        'data':data
    }
    return render(request, 'recommender/rank/index.html', context)