import networkx as nx
import random
import math

def edge_list(G):
	edges = [e for e in G.edges()]
	return edges

def min_cut(G):
	while G.number_of_nodes() > 2: 
		edge = random.choice(edge_list(G))
		G = nx.contracted_edge(G,edge, self_loops = False)
	return G

def iterated_min_cut(G):
    min_edges = []
    n = G.number_of_nodes()
    iterations = int(math.ceil(n*(n-1)*math.log(n)))
    for i in range(0,iterations):
        G_cut = min_cut(G)
        min_edges.append(G_cut.number_of_edges())
    return min(min_edges)