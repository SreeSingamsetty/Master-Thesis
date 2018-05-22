import networkx as nx
import matplotlib.pyplot as plt


g = nx.read_edgelist("concatenated_sa.csv" ,delimiter="\t")#,  nodetype=int)#, data=(('weight',float),))
h=nx.convert_node_labels_to_integers(g,label_attribute="old",first_label=1)
nx.write_edgelist(h,"edges.csv",data=False)
print(nx.info(g))
nx.draw(h,with_labels=True)
plt.show()

