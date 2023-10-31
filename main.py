import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Câmera 1
print("Informe as Coordenadas da Câmera 1")
x_cam1 = float(input("Por favor, informe a coordenada x da câmera 1: "))
y_cam1 = float(input("Agora, informe a coordenada y da câmera 1: "))

# Projeção 1
print("Informe as Coordenadas da Projeção da Câmera 1")
x_proj1 = float(input("Por favor, informe a coordenada x da projeção da câmera 1: "))
y_proj1 = float(input("Agora, informe a coordenada y da projeção da câmera 1: "))

# Câmera 2
print("Informe as Coordenadas da Câmera 2")
x_cam2 = float(input("Por favor, informe a coordenada x da câmera 2: "))
y_cam2 = float(input("Agora, informe a coordenada y da câmera 2: "))

# Projeção 2
print("Informe as Coordenadas da Projeção da Câmera 2")
x_proj2 = float(input("Por favor, informe a coordenada x da projeção da câmera 2: "))
y_proj2 = float(input("Agora, informe a coordenada y da projeção da câmera 2: "))

m_r1 = (y_proj1 - y_cam1) / (x_proj1 - x_cam1)
m_r2 = (y_proj2 - y_cam2) / (x_proj2 - x_cam2)

b_r1 = -1 * (m_r1 * x_cam1 - y_cam1)  # coeficiente linear para r1
b_r2 = -1 * (m_r2 * x_cam2 - y_cam2)  # coeficiente linear para r2
s

# Ponto de Interseção
x_i = (-(m_r2 * x_cam2) + y_cam2 + (m_r1 * x_cam1) - y_cam1) / (
    m_r1 - m_r2
)  # x da interseção

y_i = (m_r1 * x_i) - (m_r1 * x_cam1) + y_cam1  # y da interseção

# Posição do objeto reconstruído
print("Coordenada x do objeto reconstruído:", x_i)
print("Coordenada y do objeto reconstruído:", y_i)

# Gráfico 2D
x_1 = np.linspace(0, 3, 100)
y_1 = m_r1 * x_1 + b_r1

x_2 = np.linspace(0, 3, 100)
y_2 = m_r2 * x_2 + b_r2

plt.plot(x_1, y_1, label="Reta 1", color="blue")
plt.plot(x_2, y_2, label="Reta 2", color="green")
plt.scatter(
    x_i, y_i, color="red"
)  # Posição do objeto no plano xy - representada pelo ponto vermelho
plt.scatter(
    x_cam1, y_cam1, color="purple"
)  # Posição da câmera 1 no plano xy - representada pelo ponto roxo
plt.scatter(
    x_cam2, y_cam2, color="orange"
)  # Posição da câmera 2 no plano xy - representada pelo ponto laranja

plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.title("Interseção de Retas")
plt.legend()
plt.show()

# Gráfico em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Adicionando as retas
x_1_3d = np.linspace(0, 3, 100)
y_1_3d = m_r1 * x_1_3d + b_r1
z_1_3d = np.zeros_like(x_1_3d)
x_2_3d = np.linspace(0, 3, 100)
y_2_3d = m_r2 * x_2_3d + b_r2
z_2_3d = np.zeros_like(x_2_3d)

ax.plot(x_1_3d, y_1_3d, z_1_3d, label="Reta 1", color="blue")
ax.plot(x_2_3d, y_2_3d, z_2_3d, label="Reta 2", color="green")

# Adicionando os pontos
ax.scatter(x_i, y_i, 0, color="red", label="Ponto de Interseção")
ax.scatter(x_cam1, y_cam1, 0, color="purple", label="Câmera 1")
ax.scatter(x_cam2, y_cam2, 0, color="orange", label="Câmera 2")

# Configurando os rótulos
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.set_title("Interseção de Retas em 3D")
ax.legend()

# Mostrando o gráfico
plt.show()
