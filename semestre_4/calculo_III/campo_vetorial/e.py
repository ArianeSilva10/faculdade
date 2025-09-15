import numpy as np
import matplotlib.pyplot as plt

# Gera pontos de x e y
x = np.linspace(-3, 3, 20)  # 20 pontos de -3 a 3
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# Evitar divisão por zero (no ponto (0,0))
R = np.sqrt(X**2 + Y**2)
R[R == 0] = 1e-10  # evita divisão por zero

# Campo vetorial F(x,y)
U = X / R   # componente em i
V = Y / R   # componente em j

plt.figure(figsize=(6,6))
plt.quiver(X, Y, U, V, color='blue')

# Plano cartesiano
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.title('Campo Vetorial F(x,y) = (x/r, y/r)')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')  # escalas iguais
plt.show()
