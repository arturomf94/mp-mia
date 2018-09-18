import networkx as nx
import random

def edge_list(G):
	edges = [i for (i,j) in G.edges().items()]
	return edges


def min_cut(G):
	while G.number_of_edges() > 2: 
		edge = random.choice(edge_list(G))
		G = nx.contracted_edge(G,edge)
	return G