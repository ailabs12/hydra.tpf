import logging
from rdflib import Graph
import sys
logging.basicConfig(level=logging.INFO)

import hydra.tpf # required to register TPFStore plugin

URL = 'http://172.17.4.101:3001/click'
if len(sys.argv) > 1:
    URL = sys.argv[1]

g = Graph("TPFStore")
g.open(URL)

QUERY = "SELECT ?o WHERE {?s <http://www.w3.org/ns/lemon/ontolex#writtenRep> ?o FILTER (lang(?o) = 'ru')} LIMIT 100"

print (len(g))

results = g.query(QUERY)
for i in results:
    print (i)
