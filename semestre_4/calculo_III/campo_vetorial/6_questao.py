import numpy as np
import matplotlib.pyplot as plt

# Criar uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 1️⃣ Pontos no primeiro octante da esfera x^2 + y^2 + z^2 = 1
# Vamos usar coordenadas esféricas para gerar pontos
phi = np.linspace(0, np.pi/2, 5)      # ângulo azimutal
theta = np.linspace(0, np.pi/2, 5)    # ângulo polar
phi, theta = np.meshgrid(phi, theta)

x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# 2️⃣ Vetores do gradiente F(x, y, z) = (2x, 2y, 2z)
u = 2*x
v = 2*y
w = 2*z

# 3️⃣ Desenhar os vetores
ax.quiver(x, y, z, u, v, w, length=0.2, color='blue', normalize=True)

# 4️⃣ Ajustes do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gradiente na superfície da esfera (primeiro octante)')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)
plt.show()
