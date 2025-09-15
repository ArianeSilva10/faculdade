import numpy as np
import matplotlib.pyplot as plt

# Definir grid de pontos (x,y)
x = np.linspace(-1, 1, 15)
y = np.linspace(-0.5, 3, 15)
X, Y = np.meshgrid(x, y)

# Campo vetorial V(x,y) = (0, 1 - x^2)
U = np.zeros_like(X)          # componente x = 0
V = 1 - X**2                  # componente y

plt.figure(figsize=(6,6))
plt.quiver(X, Y, U, V, angles='xy')
plt.title(r"Campo vetorial $\vec V(x,y)=(0,1-x^2)$ para |x|≤1")
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1.2,1.2)
plt.ylim(-0.5,3.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.show()
