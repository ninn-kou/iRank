from StageTwo import *
from DataLoading import *

path1 = '../datasets/Alaska/Kaktovi.edges.csv'
network1, g1, nodesLayers1 = loadAlaskaDataIntoNetwork(path1)

lam1 = 0.5
sig1 = 0.5
xbar1 = np.ones(g1, dtype=object)
for layer1 in range(g1):
    # xbar1[layer1] = np.random.rand(nodesLayers1[layer1])
    xbar1[layer1] = np.ones(nodesLayers1[layer1])
Alaska = stage2(network1, nodesLayers1, lam1, sig1, xbar1)

path2 = '../datasets/EUAir/EUAirTransportation_multiplex.csv'
network2, g2, nodesLayers2 = loadEUAirTransportDataIntoNetwork(path2)

lam2 = 0.5
sig2 = 0.5
xbar2 = np.ones(g2, dtype=object)
for layer2 in range(g2):
    # xbar2[layer2] = np.random.rand(nodesLayers2[layer2])
    xbar2[layer2] = np.ones(nodesLayers2[layer2])
EUAir = stage2(network2, nodesLayers2, lam2, sig2, xbar2)
