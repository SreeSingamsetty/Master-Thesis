from rdflib import Graph

g = Graph()
g.parse("short_abstracts_copy.ttl", format="ttl")
g.serialize("short_abstracts_copy.csv", format="ttl", base="http://dbpedia.org/resource/")
