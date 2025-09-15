import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Pontos da hipérbole xy = 1, x > 0
x = np.linspace(0.1, 3, 10)  # evita x = 0
y = 1 / x

# 2️⃣ Componentes do vetor g(x, y) = (1, xy)
u = np.ones_like(x)  # componente x do vetor
v = x * y            # componente y do vetor (sempre 1 na hipérbole)

# 3️⃣ Desenhar a hipérbole
plt.plot(x, y, 'ro', label='Hipérbole xy=1')

# 4️⃣ Desenhar os vetores
plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1, color='blue')

# 5️⃣ Ajustes do gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo vetorial sobre a hipérbole xy=1')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
