import networkx as nx
import matplotlib.pyplot as plt
import collections


G1 = nx.gnp_random_graph(10**4, 0.1)
degree_sequence = sorted([d for n, d in G1.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.title("Degree Histogram (n=10^4, p=0.1)")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()


G2 = nx.gnp_random_graph(10**4, 1/(10**4))
degree_sequence = sorted([d for n, d in G2.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.title("Degree Histogram (n=10^4, p=1/10^4)")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()


G3 = nx.gnp_random_graph(10**4, 1/(10**8))
degree_sequence = sorted([d for n, d in G3.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.title("Degree Histogram (n=10^4, p=1/10^8)")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()
