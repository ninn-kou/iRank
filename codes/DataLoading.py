import numpy as np
import csv

def loadAMiner(path):
    filename = open(path, 'r')
    file = csv.reader(filename)

    # g = 2 which indicates the number of layers.
    # Saving memory.
    g = 2

    nodesLayers = []
    for i in range(g):
        nodesLayers.append(set())

    # How to keep my file opening?

    filename = open(path, 'r')
    file = csv.reader(filename)
    for row in file:
        nodesLayers[np.int32(row[1]) - 1].add(np.int32(row[0]))
        nodesLayers[np.int32(row[3]) - 1].add(np.int32(row[2]))
    for layer in range(g):
        nodesLayers[layer] = max(nodesLayers[layer])

    network = np.zeros((g, g), dtype=object)

    for row in range(g):
        for col in range(g):
            network[row][col] = np.zeros((nodesLayers[row], nodesLayers[col]), dtype=np.int32)

    filename = open(path, 'r')
    file = csv.reader(filename)
    for row in file:
        # Undirected Graph so ""
        network[np.int32(row[1]) - 1][np.int32(row[3]) - 1][np.int32(row[0]) - 1][np.int32(row[2]) - 1] = bool(row[4])

    return network, g, nodesLayers

def loadAlaska(path):
    """Alaska Multiplex Networks
        URL:
            <https://github.com/manlius/Alaska>
        TAGS:
            Multiplex,
            Directed,
            Weighted
    """
    filename = open(path, 'r')
    file = csv.reader(filename)

    layerFrom = set()
    layerTo = set()
    for row in file:
        layerFrom.add(int(row[1]))
        layerTo.add(int(row[3]))

    g = max(max(layerFrom), max(layerTo))

    nodesLayers = []
    for i in range(g):
        nodesLayers.append(set())

    # How to keep my file opening?

    filename = open(path, 'r')
    file = csv.reader(filename)
    for row in file:
        nodesLayers[int(row[1]) - 1].add(int(row[0]))
        nodesLayers[int(row[3]) - 1].add(int(row[2]))
    for layer in range(g):
        nodesLayers[layer] = max(nodesLayers[layer])

    network = np.zeros((g, g), dtype=object)

    for row in range(g):
        for col in range(g):
            network[row][col] = np.zeros((nodesLayers[row], nodesLayers[col]), dtype=float)

    filename = open(path, 'r')
    file = csv.reader(filename)
    for row in file:
        # Undirected Graph so ""
        network[int(row[1]) - 1][int(row[3]) - 1][int(row[0]) - 1][int(row[2]) - 1] = float(row[4])

    return network, g, nodesLayers

def loadMultiplex(path):
    filename = open(path, 'r')
    file = csv.reader(filename)

    layers = set()
    nodes = set()
    for row in file:
        layers.add(int(row[0]))
        nodes.add(int(row[1]))
        nodes.add(int(row[2]))

    g = max(layers)
    n = max(nodes)

    nodesLayers = [n] * g

    network = np.zeros((g, g), dtype=object)

    for row in range(g):
        for col in range(g):
            network[row][col] = np.zeros((n, n), dtype=float)

    filename = open(path, 'r')
    file = csv.reader(filename)

    for row in file:
        currLayer = int(row[0]) - 1
        network[currLayer][currLayer][int(row[1]) - 1][int(row[2]) - 1] = float(row[3])
        network[currLayer][currLayer][int(row[2]) - 1][int(row[1]) - 1] = float(row[3])

    return network, g, nodesLayers
