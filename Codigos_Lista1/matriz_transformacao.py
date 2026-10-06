import math


def matriz_transformacao(theta1, theta2):
    L1 = 20.0
    L2 = 15.0

    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)

    theta = theta1 + theta2

    x = L1 * math.cos(theta1) + L2 * math.cos(theta)
    y = L1 * math.sin(theta1) + L2 * math.sin(theta)

    T = [
        [math.cos(theta), -math.sin(theta), x],
        [math.sin(theta),  math.cos(theta), y],
        [0,                 0,               1]
    ]

    return T


theta1 = float(input("Digite o ângulo theta1 (em graus): "))
theta2 = float(input("Digite o ângulo theta2 (em graus): "))

T = matriz_transformacao(theta1, theta2)

print("\nMatriz de transformação:")

for linha in T:
    print([round(valor, 4) for valor in linha])