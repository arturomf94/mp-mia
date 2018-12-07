import networkx as nx

def create_graph(image):
    # Create grid
    height, width = image.shape
    G = nx.grid_2d_graph(height, width)
    G = G.to_directed()
    # Add source and sink
    G.add_node(0)
    G.add_node(1)
    nodes = [node for node in G.nodes()]
    # Add edges for source and sink
    for node in nodes:
        if isinstance(node, tuple):
            G.add_edge(0, node, capacity = 0)
            G.add_edge(node, 1, capacity = 0)
    return G

def add_costs(G, unary_cost_source, unary_cost_sink, pairwise_cost):
    edges = [edge for edge in G.edges()]
    for edge in edges:
        if isinstance(edge[0], tuple) and isinstance(edge[1], tuple):
            G[edge[0]][edge[1]]['capacity'] = pairwise_cost
        elif isinstance(edge[0], tuple) and not isinstance(edge[1], tuple):
            G[edge[0]][edge[1]]['capacity'] = unary_cost_sink
        else:
            G[edge[0]][edge[1]]['capacity'] = unary_cost_source
