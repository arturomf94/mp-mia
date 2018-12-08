import networkx as nx

def create_graph(image):
    # Create grid
    height, width = image.shape
    G = nx.grid_2d_graph(height, width)
    G = G.to_directed()
    # Add source and sink
    G.add_node(0) # Sink
    G.add_node(1) # Source
    nodes = [node for node in G.nodes()]
    # Add edges for source and sink and attributes
    for node in nodes:
        if isinstance(node, tuple):
            if image[node[0]][node[1]] == 0:
                G.node[node].update({'value': 0})
            else:
                G.node[node].update({'value': 1})
            G.add_edge(node, 0, capacity = 0)
            G.add_edge(1, node, capacity = 0)
        else:
            if node == 0:
                G.node[node].update({'value': 0})
            else:
                G.node[node].update({'value': 1})
    return G

def add_costs(G, unary_matching_cost_source,
                unary_nonmatching_cost_source,
                unary_matching_cost_sink,
                unary_nonmatching_cost_sink,
                pairwise_cost):
    edges = [edge for edge in G.edges()]
    for edge in edges:
        if isinstance(edge[0], tuple) and isinstance(edge[1], tuple):
            if G.node[edge[0]]['value'] == G.node[edge[0]]['value']:
                G[edge[0]][edge[1]]['capacity'] = 0
            else:
                G[edge[0]][edge[1]]['capacity'] = pairwise_cost
        elif isinstance(edge[0], tuple) and not isinstance(edge[1], tuple):
            if G.node[edge[0]]['value'] == G.node[edge[0]]['value']:
                G[edge[0]][edge[1]]['capacity'] = unary_matching_cost_sink
            else:
                G[edge[0]][edge[1]]['capacity'] = unary_nonmatching_cost_sink
        else:
            if G.node[edge[0]]['value'] == G.node[edge[0]]['value']:
                G[edge[0]][edge[1]]['capacity'] = unary_matching_cost_source
            else:
                G[edge[0]][edge[1]]['capacity'] = unary_nonmatching_cost_source

# def recover_image(image, partition):
#     clean_image = image
#     if 0 in partition[0]:
