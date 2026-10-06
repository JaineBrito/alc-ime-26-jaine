def substituicao_regressiva(A, b):
    x = [0] * len(A)

    for i in range(len(A) - 1, -1, -1):

        if A[i][i] == 0:
            raise Exception("Elemento nulo na diagonal")

        soma = 0

        for j in range(i + 1, len(A)):
            soma = soma + A[i][j] * x[j]

        x[i] = (b[i] - soma) / A[i][i]

    return x


# Entrada da matriz
n = int(input("Digite o tamanho da matriz: "))

A = []

for i in range(n):
    linha = list(map(float, input(f"Digite a linha {i + 1}: ").split()))

    if len(linha) != n:
        raise Exception("A linha da matriz deve ter tamanho correspondente à matriz")

    A.append(linha)


# Entrada do vetor coluna b
b = []

for i in range(n):
    b.append(float(input(f"Digite b[{i + 1}]: ")))


# Executa a função
resultado = substituicao_regressiva(A, b)

print("Solução:", resultado)