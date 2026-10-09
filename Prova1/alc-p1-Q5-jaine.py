import numpy as np


def substituicao_progressiva(L, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        soma = 0.0

        for j in range(i):
            soma += L[i, j] * y[j]

        y[i] = b[i] - soma

    return y


def substituicao_regressiva(U, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        if U[i, i] == 0:
            raise Exception(
                "Pivô nulo encontrado. "
                "Utilize uma função alternativa com pivoteamento para resolver o sistema."
            )

        soma = 0.0

        for j in range(i + 1, n):
            soma += U[i, j] * x[j]

        x[i] = (y[i] - soma) / U[i, i]

    return x


def resolve_lu(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2:
        raise ValueError("A matriz A deve ser bidimensional.")

    if A.shape[0] != A.shape[1]:
        raise ValueError("A matriz A deve ser quadrada.")

    n = A.shape[0]

    if b.ndim != 1:
        raise ValueError("O vetor b deve ser unidimensional.")

    if b.shape[0] != n:
        raise ValueError("O vetor b deve ter o mesmo tamanho da matriz A.")

    L = np.eye(n)
    U = np.array(A, dtype=float)

    for j in range(n):

        if U[j, j] == 0:
            raise Exception(
                "Pivô nulo encontrado na decomposição LU. "
                "Utilize uma função alternativa com pivoteamento para resolver o sistema."
            )

        for k in range(j + 1, n):

            L[k, j] = U[k, j] / U[j, j]

            for i in range(j + 1, n):
                U[k, i] = U[k, i] - L[k, j] * U[j, i]

            U[k, j] = 0.0

    y = substituicao_progressiva(L, b)
    x = substituicao_regressiva(U, y)

    return L, U, x


if __name__ == "__main__":
    A = [
        [2.0, 1.0, 1.0],
        [4.0, 3.0, 3.0],
        [8.0, 7.0, 9.0],
    ]

    b = [1.0, 1.0, 1.0]

    L, U, x = resolve_lu(A, b)

    print("L =")
    print(L)

    print("\nU =")
    print(U)

    print("\nx =")
    print(x)