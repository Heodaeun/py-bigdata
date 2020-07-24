import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for i in range(1,501):
	G.add_node(i)

	
for i in range(1,501):
	for j in range(1,501):
		if i%3 == 0:
			G.add_edge(i, 3*j)
		elif i%4 == 0:
			G.add_edge(i, 4*j)
		elif i%7 == 0:
			G.add_edge(i, 7*j)


nx.draw(G)
plt.show()
