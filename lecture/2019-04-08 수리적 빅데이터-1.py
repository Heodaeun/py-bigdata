import networkx as nx
import csv

G = nx.gnp_random_graph(100, 0.1)

Gedge = G.edges

f = open("network.csv","w",encoding="utf-8",newline="")
wr = csv.writer(f)
for Edge in Gedge:
    wr.writerow([Edge[0],Edge[1]])
f.close()
print(G.edges)