import networkx as nx
import csv
import matplotlib.pyplot as plt
import collections

G = nx.Graph()

f = open('network2.csv','r')
csvReader = csv.reader(f)

weight=0

for row in csvReader:
    G.add_edge(int(row[0]),int(row[1]))

f.close()
print(G.edges)
nx.draw(G)
plt.show()


degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.bar(deg,cnt)
plt.title("network2")
plt.ylabel("count")
plt.xlabel("degree")
plt.show()

B = nx.betweenness_centrality(G)
C = nx.closeness_centrality(G)

node = B.keys()
betweenness = B.values()
plt.bar(node, betweenness)
plt.title("network2-betweenness centrality")
plt.ylabel("betweenness centrality")
plt.xlabel("node")
plt.show()

node2 = C.keys()
closeness = C.values()
plt.bar(node2, betweenness)
plt.title("network2-closeness centrality")
plt.ylabel("closeness")
plt.xlabel("node")
plt.show()