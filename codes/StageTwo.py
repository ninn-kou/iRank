import numpy as np


def inverseSR(diagonal):
    """
    Inverse Square Root for Symmetrically normalized Laplacian matrix, skip all "0" in ndarray.
    """
    for val in range(len(diagonal)):
        diagonal[val] = diagonal[val] ** (-0.5) if diagonal[val] else 0
    return diagonal


def stage2(network, H, lam, sig, xbar):
    """
    network:
        a numpy 2d array (layer_numbers * layer_numbers), and each element is a numpy 2d array (nodes_of_layer_row * nodes_of_layer_col).
    H:
        (1 * g) ndarray, number of nodes in each layer.
    lam:
        a float for parameter lambda.
    sig:
        a float for parameter sigma.
    xbar:
        a numpy 1d array (layer_numbers), and each element is a numpy 1d array (nodes_of_layer).
    """

    # Number of layers
    g = network.shape[0]

    # Dependencies Matrix G
    # Shape: (g * g)
    G = np.zeros((g, g))
    for i in range(g):
        for j in range(g):
            G[i][j] = np.sum(network[i][j])
            if G[i][j] != 0:
                G[i][j] = 1

    A = np.diagonal(network)

    # isr: Inverse Square Root
    D_within_isr = np.ones(g, dtype=object)
    for layer in range(g):
        d_layer = np.sum(A[layer], axis=0)
        d_layer = inverseSR(d_layer)
        d_layer = np.diag(d_layer)
        D_within_isr[layer] = d_layer

    S_within = np.ones(g, dtype=object)
    for layer in range(g):
        s_layer = D_within_isr[layer] @ A[layer] @ D_within_isr[layer]
        S_within[layer] = s_layer

    D_cross_out = np.ones((g, g), dtype=object)
    D_cross_in = np.ones((g, g), dtype=object)
    for alpha in range(g):
        for beta in range(g):
            d_alphabeta = np.sum(network[alpha][beta], axis=1)
            d_alphabeta = inverseSR(d_alphabeta)
            d_alphabeta = np.diag(d_alphabeta)
            D_cross_out[alpha][beta] = d_alphabeta

            d_betaalpha = np.sum(network[alpha][beta], axis=0)
            d_betaalpha = inverseSR(d_betaalpha)
            d_betaalpha = np.diag(d_betaalpha)
            D_cross_in[alpha][beta] = d_betaalpha

    S_cross = np.ones((g, g), dtype=object)
    for alpha in range(g):
        for beta in range(g):
            S_cross[alpha][beta] = (
                D_cross_out[alpha][beta]
                @ network[alpha][beta]
                @ D_cross_in[alpha][beta]
            )

    X = np.ones(g, dtype=object)
    for layer in range(g):
        # X[layer] = np.random.rand(H[layer])
        X[layer] = np.ones(H[layer])

    for alpha in range(g):
        temp_cross = 0
        for beta in range(g):
            temp_cross += G[alpha][beta] * (S_cross[alpha][beta] @ X[beta])
        X[alpha] = (
            lam * (S_within[alpha] @ X[alpha])
            + sig * temp_cross
            + (1 - lam - sig) * xbar[alpha]
        )

    return X
