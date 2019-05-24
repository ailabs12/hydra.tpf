import hydra.tpf # ensures that the TPFStore plugin is registered
from rdflib import Graph

g = Graph('TPFStore')
g.open('http://data.linkeddatafragments.org/dbpedia2014')

results = g.query("SELECT DISTINCT ?cls { [ a ?cls ] } LIMIT 10")
print(results)
