import hydra.tpf # ensures that the TPFStore plugin is registered
from rdflib import Graph

g = Graph('TPFStore')
g.open('http://172.17.4.101:3001/click')
results = g.query("SELECT ?o WHERE {?s <http://www.w3.org/ns/lemon/ontolex#writtenRep> ?o FILTER (lang(?o) = 'ru')} LIMIT 100")

print (len(g))

for i in results:
    print (i[0])
