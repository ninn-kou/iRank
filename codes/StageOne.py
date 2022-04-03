import numpy as np

# TODO: Iterations not working.

def stage1(Network, Size, a, s, gamma, delta=0.85):
    """
    H:
        (1 * g) ndarray, number of nodes in each layer.
    """

    v_quadratic_error = 0.0001

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
    Z = np.random.uniform(0, 1, g)

    G = np.zeros((n, n), dtype=float)
    for layer in range(g):
        G += A[layer] * Z[layer]

    # Centrality of node initialized as 0.
    X = np.random.uniform(0, 1, n)

    # V_i initialized as 0.
    V = np.zeros(n, dtype=float)
    # V_i = \sum^{g}_{j=1} [G_{ij} + G_{ji}
    V = np.sum(G, axis=1) + np.sum(G, axis=0)
    # Apply θ: Heaviside step function to array V.
    V = np.where(V <= 0, 0, V)

    # 1st Iteration by using random values of X and Z.

    beta = np.sum((1 - delta * (np.sum(G, axis=0) > 1)) * X) / np.sum(V)

    # We need another variable to store the value of X at the beginning of
    # each iteration because X value only changes when moving to the next
    # iteration but is not in progress.
    X_constant = X
    for layer in range(g):
        X += B[layer] * X_constant / np.sum(B[layer])
    X += V * beta
    X /= np.sum(X)

    for layer in range(g):
        Z[layer] = (W[layer] ** a) * (np.sum(B[layer] * (X ** (s * gamma))) ** s)
    Z /= np.sum(Z)

    # Iterations.
    while np.linalg.norm(X - X_constant, 2) > v_quadratic_error * np.linalg.norm(X):
        beta = np.sum((1 - delta * (np.sum(G, axis=0) > 1)) * X) / np.sum(V)
        X_constant = X
        for layer in range(g):
            X += B[layer] * X_constant / np.sum(B[layer])
        X += V * beta
        X /= np.sum(X)
        for layer in range(g):
            Z[layer] = (W[layer] ** a) * (np.sum(B[layer] * (X ** (s * gamma))) ** s)
        Z /= np.sum(Z)

    return X, Z
