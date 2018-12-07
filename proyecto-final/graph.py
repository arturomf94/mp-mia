import networkx as nx

def create_graph(image):
    height, width = image.shape
    G = nx.grid_2d_graph(height, width)
    G = G.to_directed()
    return G
