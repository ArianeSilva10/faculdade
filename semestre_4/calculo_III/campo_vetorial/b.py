import numpy as np
import matplotlib.pyplot as plt

# Criando um grid de pontos
X, Y = np.meshgrid(np.arange(-5, 6, 1), np.arange(-5, 6, 1))

# Campo vetorial: F(x,y) = i + j
U = np.ones_like(X)  # componente x
V = np.ones_like(Y)  # componente y

plt.figure(figsize=(6,6))
plt.quiver(X, Y, U, V, color='blue')
plt.title('Campo Vetorial: î + ĵ')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()
