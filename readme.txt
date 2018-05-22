Dataset: 

Short Abstracts dataset from  http://wiki.dbpedia.org/Downloads2015-10 

sample triple: 

<Aardwolf> rdfs:comment "The aardwolf (Proteles cristata) is a small, insectivorous mammal, native to East Africa and Southern Africa. Its name means \"earth wolf\" in the Afrikaans / Dutch language. It is also called \"maanhaar jackal\" (Literally \"mane jackal\" in Afrikaans) or civet hyena, based on the secretions reminiscent of civets from their anal glands. The aardwolf is in the same family as the hyenas."@en .


Here, for trail purpose, I made a copy of the the above dataset (first 103 triples) and made an edge list from it.

Steps: 

1.Converting .ttl file to .csv : rdfttl_to_csv.py  input: short_abstracts_copy.ttl output: short_abstracts_copy.csv

2.Because this file has '\"' (Ex:\"earth wolf\"), when reading a file these words are being read as a separate entity, I have replaced '\"' with space manually, so that the whole object is read as a single entity. This part, however, I will implement in the code when I proceed with next steps.

3.Making this as a tab separated file: tabseparated_csv.py  input: short_abstracts_copy.csv output: short_abstracts_copy_tab.csv

4.Extracting subject and object from this file :extracting_subject_object.py  input: short_abstracts_copy_tab.csv output:concatenated_sa.csv

5.Creating an edge list with numbers as node labels : edgelist_from_graph.py input: concatenated_sa.csv output: edges.csv


This edgelist will be the input for node-to-vec 



