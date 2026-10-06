import numpy as np

valores_n = [5, 15, 25]

for n in valores_n:

    u = np.random.rand(n, 1)
    v = np.random.rand(n, 1)

    A = u @ v.T

    rank_A = np.linalg.matrix_rank(A)

    norma_u = np.linalg.norm(u, 2)
    norma_v = np.linalg.norm(v, 2)

    produto_normas = norma_u * norma_v

    norma_A = np.linalg.norm(A, 2)

    nullidade_A = n - rank_A

    print(f"\nn = {n}")
    print(f"rank(u v^T) = {rank_A}")
    print(f"||u||_2 ||v||_2 = {produto_normas:.6f}")
    print(f"||u v^T||_2 = {norma_A:.6f}")
    print(f"nullidade(u v^T) = {nullidade_A}")

    assert rank_A == 1
    assert rank_A + nullidade_A == n
    assert np.isclose(norma_A, produto_normas)