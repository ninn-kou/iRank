import numpy as np


def stage1(Network, Size, a, s, gamma, delta=0.85):
    """
    Network:
        (g * n * n) ndarray, g layers adjacency matrices.
    Size:
        (g) ndarray, number of nodes in each layer.
    a: the influence of a layer is
        (a = 1) proportional to W[layer].
        (a = 0) normalized with respect to W[layer].
    s: layers have larger influence if they include
        (s = 1)  more central nodes.
        (s = -1) fewer highly influential nodes.
    gamma:
        (gamma > 1) enhance the contribution of low centrality nodes for Z calculation.
        (gamma < 1) suppress the contribution of low centrality nodes for Z calculation.
    delta:
        (delta = 0.85) as usual in the context of the PageRank algorithms.
    """

    error = 1e-6

    g = len(Size)
    n = Size[0]
    A = np.diagonal(Network)

    W = np.zeros(g, dtype=float)
    for layer in range(g):
        W[layer] = np.sum(A[layer])

    B = np.zeros((g, n), dtype=float)
    for layer in range(g):
        B[layer] = np.sum(A[layer], axis=0) / W[layer]

    # Centrality of layer initialized as 0.
    # Z = np.random.uniform(0, 1, g)
    # Set the initial Z value as a constant to avoid random effects when calculation
    # from (gamma == 0.1) to (gamma == 3.0).
    Z = np.full(g, 0.5)

    G = np.zeros((n, n), dtype=float)
    for layer in range(g):
        G += A[layer] * Z[layer]

    # Centrality of node initialized as 0.
    # X = np.random.uniform(0, 1, n)
    # Set the initial X value as a constant to avoid random effects when calculation
    # from (gamma == 0.1) to (gamma == 3.0).
    X = np.full(n, 0.5)

    # V_i initialized as 0.
    V = np.zeros(n, dtype=float)
    # V_i = \sum^{g}_{j=1} [G_{ij} + G_{ji}
    V = np.sum(G, axis=1) + np.sum(G, axis=0)
    # Apply theta (Heaviside step function) to array V.
    V = np.where(V <= 0, 0, V)

    # Iterations stop when related error is less than setting value.
    while True:
        beta = np.sum((1 - delta * (np.sum(G, axis=0) > 1)) * X) / np.sum(V)

        X_constant = X
        X = np.zeros(n, dtype=float)
        for layer in range(g):
            X += B[layer] * X_constant / np.sum(B[layer])
        X += V * beta
        X /= np.sum(X)

        Z = np.zeros(g, dtype=float)
        # Handle with ZeroDivisionError for (0 ** -1).
        X_not_zero = np.copy(X)
        X_not_zero[X_not_zero == 0] = 1
        for layer in range(g):
            Z[layer] = (W[layer] ** a) * (np.sum(B[layer] * (X_not_zero ** (s * gamma))) ** s)
        Z /= np.sum(Z)

        # Stopping condition.
        if np.average(np.absolute(X - X_constant)) < error:
            break

    return X, Z
