import numpy as np


def is_orthogonal_by_vectors(A):

    A = np.asarray(A, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A matriz deve ser quadrada.")

    # Verifica se todas as colunas possuem norma 2 igual a 1
    for j in range(A.shape[1]):
        if not np.isclose(np.linalg.norm(A[:, j], 2), 1.0, atol=1e-4):
            return False

    # Verifica se as colunas são ortogonais duas a duas
    for i in range(A.shape[1]):
        for j in range(i + 1, A.shape[1]):
            if not np.isclose(np.dot(A[:, i], A[:, j]), 0.0, atol=1e-4):
                return False

    return True


# Matrizes do exercício 6.38
P1_638 = np.array([
    [-0.40825,  0.43644,  0.80178],
    [-0.81650,  0.21822, -0.53452],
    [-0.40825, -0.87287,  0.26726]
])

P2_638 = np.array([
    [-0.51450,  0.48507,  0.70711],
    [-0.68599, -0.72761,  0.00000],
    [ 0.51450, -0.48507,  0.70711]
])


# Matrizes do exercício 6.39
P1_639 = np.array([
    [-0.58835,  0.70206,  0.40119],
    [-0.78446, -0.37524, -0.49377],
    [-0.19612, -0.60523,  0.77152]
])

P2_639 = np.array([
    [-0.47624, -0.42640,  0.30151],
    [ 0.087932,  0.86603, -0.40825],
    [-0.87491, -0.26112,  0.86164]
])


print("Exercício 6.38")
print("P1:", is_orthogonal_by_vectors(P1_638))
print("P2:", is_orthogonal_by_vectors(P2_638))

print("\nExercício 6.39")
print("P1:", is_orthogonal_by_vectors(P1_639))
print("P2:", is_orthogonal_by_vectors(P2_639))