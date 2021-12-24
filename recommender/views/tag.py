import json
from django.shortcuts import render
from neo4j import GraphDatabase

def tag(request):
    graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","1234"))
    session = graphdb.session()
    query = "MATCH(m:Movie)-[r:isTaggedBy]->(u:User) RETURN u.ID AS id_user, m.ID AS id_movie, m.Title AS title, collect(r.Tag) AS tag ORDER BY id_user"
    nodes = session.run(query)
    data = json.dumps(nodes.data())
    data = json.loads(data)
    context ={
        'isTag' : True,
        'title':'Tag',
        'data':data
    }
    return render(request, 'recommender/tag/index.html', context)