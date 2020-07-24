import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np

G = nx.gnp_random_graph(100, 0.01)
print(G.edges())

A = []
print(np.array(G.edges()))
#print(list(G[0].keys()))
#for i in range(99):
#    for j in (list(G[i].keys())):
#        A[i][j] = 1

print(A)

#for i in range(G[99]):
#    for j in range(G[99].):
#        j = j+1
#    i = i+1

#print(G)

a = [[1,2,3],[4,5,6]]
b = a.reverse()
c = a*b
print(c)