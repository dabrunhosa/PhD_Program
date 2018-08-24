import networkx as nx
import matplotlib.pyplot as plt
from MultiSynapse_Program import Multi_Mapping

mg = Multi_Mapping()
mg.readFile('all_process_connections.txt')
pos = nx.spring_layout(mg.synapse_graph)

# nodes
plt.figure(num=None, figsize=(300, 300), dpi=100, facecolor='w', edgecolor='k')
nx.draw_networkx_nodes(mg.synapse_graph, pos, node_size=400)

# edges
nx.draw_networkx_edges(mg.synapse_graph, pos, width=1.2)

# labels for the nodes
nx.draw_networkx_labels(mg.synapse_graph, pos, font_size=13,
                                         font_family='sans-serif')

#plt.savefig('multiGraph.pdf')
plt.show()
