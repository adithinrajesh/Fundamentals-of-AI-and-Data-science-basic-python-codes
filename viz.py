import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, explored_nodes, frontier_nodes):
    G = nx.Graph(graph)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=1.0)

    nx.draw_networkx_nodes(G, pos, nodelist=explored_nodes, node_color='green', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=frontier_nodes, node_color='yellow', node_size=700)

    plt.title("Graph Visualization")
    plt.show()

# Example usage:
graph_example = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': [],
    'e': ['h', 'i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []
}

explored_example = ['a', 'b', 'c']
frontier_example = ['d', 'e']

visualize_graph(graph_example, explored_example, frontier_example)
