import numpy as np


def is_orthogonal_by_definition(A):

    A = np.asarray(A, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A matriz deve ser quadrada.")

    n = A.shape[0]
    I = np.eye(n)

    return np.allclose(A.T @ A, I, atol=1e-4)


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
print("P1:", is_orthogonal_by_definition(P1_638))
print("P2:", is_orthogonal_by_definition(P2_638))

print("\nExercício 6.39")
print("P1:", is_orthogonal_by_definition(P1_639))
print("P2:", is_orthogonal_by_definition(P2_639))