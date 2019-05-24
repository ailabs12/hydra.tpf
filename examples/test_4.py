import hydra.tpf # ensures that the TPFStore plugin is registered
from rdflib import Graph

g = Graph('TPFStore')
g.open('http://172.17.4.101:3001/click')

QUERY = """
SELECT * WHERE {
  ?s ?p ?o
}
LIMIT 100
"""

results = g.query(QUERY)

for i in results:
  print(i[0])
