import math


def posicao_robo(theta1, theta2):
    L1 = 20.0
    L2 = 15.0

    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)

    x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
    y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

    return round(x, 1), round(y, 1)


theta1 = float(input("Digite o ângulo theta1 (em graus): "))
theta2 = float(input("Digite o ângulo theta2 (em graus): "))

x, y = posicao_robo(theta1, theta2)

print(f"X_U = {x:.1f} cm")
print(f"Y_U = {y:.1f} cm")