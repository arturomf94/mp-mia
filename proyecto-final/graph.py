import networkx as nx

def create_graph(image):
    # Create grid
    height, width = image.shape
    G = nx.grid_2d_graph(height, width)
    G = G.to_directed()
    G.add_node(0)
    G.add_node(1)
    nodes = [node for node in G.nodes()]
    for node in nodes:
        if isinstance(node, tuple):
            G.add_edge(0, node)
            G.add_edge(node, 1)
    return G
