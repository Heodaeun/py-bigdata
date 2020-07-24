import networkx as nx
import csv

G = nx.Graph()

f = open('network.csv','r')
csvReader = csv.reader(f)

for row in csvReader:
    G.add_edge(int(row[0]),int(row[1]))

f.close()
print(G.edges)