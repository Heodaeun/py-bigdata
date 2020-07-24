import networkx as nx
import csv
import matplotlib.pyplot as plt
import collections

G = nx.Graph()

f = open('DAEGU_LINK.csv','r')
csvReader = csv.reader(f)

print(type(csvReader))

for row in csvReader:
    if row[1] != 'Source':
        G.add_edge(int(row[1]),int(row[2]))
f.close()
print(G.edges)
nx.draw(G)
plt.show()

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.title("DAEGU_LINK")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()

B = nx.betweenness_centrality(G)
C = nx.closeness_centrality(G)

node = B.keys()
betweenness = B.values()
plt.bar(node, betweenness)
plt.title("DAEGU_LINK-betweenness centrality")
plt.ylabel("betweenness centrality")
plt.xlabel("node")
plt.show()

node2 = C.keys()
closeness = C.values()
plt.bar(node2, betweenness)
plt.title("DAEGU_LINK-closeness centrality")
plt.ylabel("closeness")
plt.xlabel("node")
plt.show()