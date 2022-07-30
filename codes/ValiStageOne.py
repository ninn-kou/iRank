import numpy as np
import networkx as nx


def s1_betweenness_centrality(Network, Size):
    """Calculate the betweenness centrality of each node in the network.
    Network:
        (g * n * n) ndarray, g layers supra adjacency matrices.
    Size:
        (g) ndarray, number of nodes in each layer.
    """
    nx_betweenness_centrality = np.zeros(Size[0], dtype=float)
    for layer in range(len(Size)):
        G = nx.from_numpy_array(Network[layer][layer])
        T = nx.betweenness_centrality(G, normalized=True)
        for node in range(Size[0]):
            nx_betweenness_centrality[node] += T[node]
    return nx_betweenness_centrality


def s1_closeness_centrality(Network, Size):
    """Calculate the closeness centrality of each node in the network.
    Network:
        (g * n * n) ndarray, g layers supra adjacency matrices.
    Size:
        (g) ndarray, number of nodes in each layer.
    """
    nx_closeness_centrality = np.zeros(Size[0], dtype=float)
    for layer in range(len(Size)):
        G = nx.from_numpy_array(Network[layer][layer])
        T = nx.closeness_centrality(G)
        for node in range(Size[0]):
            nx_closeness_centrality[node] += T[node]
    return nx_closeness_centrality


def s1_degree_centrality(Network, Size):
    """Calculate the degree centrality of each node in the network.
    Network:
        (g * n * n) ndarray, g layers supra adjacency matrices.
    Size:
        (g) ndarray, number of nodes in each layer.
    """
    nx_degree_centrality = np.zeros(Size[0], dtype=float)
    for layer in range(len(Size)):
        G = nx.from_numpy_array(Network[layer][layer])
        T = nx.degree_centrality(G)
        for node in range(Size[0]):
            nx_degree_centrality[node] += T[node]
    return nx_degree_centrality


def s1_eigenvector_centrality(Network, Size):
    """Calculate the eigenvector centrality of each node in the network.
    Network:
        (g * n * n) ndarray, g layers supra adjacency matrices.
    Size:
        (g) ndarray, number of nodes in each layer.
    """
    nx_eigenvector_centrality = np.zeros(Size[0], dtype=float)
    for layer in range(len(Size)):
        G = nx.from_numpy_array(Network[layer][layer])
        T = nx.eigenvector_centrality_numpy(G)
        for node in range(Size[0]):
            nx_eigenvector_centrality[node] += T[node]
    return nx_eigenvector_centrality
