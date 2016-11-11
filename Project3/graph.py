
# Bibliotecas importadas
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Variaveis
N = 10                              # Numero de nodos
P = 0.1                             # Probabilidade de conexao

# Criando a matriz
matrizAdj = np.random.rand(N, N)    # Matriz Adjacencia

# Preenchendo a matriz
for i in range(N):
    for j in range(i, N):
        if matrizAdj[i][j] <= P: matrizAdj[i][j] = 1
        else: matrizAdj[i][j] = 0


# Ajustando a simetria da matriz
for i in range(N):
    for j in range(0, i):
        matrizAdj[i][j] = matrizAdj[j][i]


# Plotando a matriz adjacencia
print(matrizAdj)

# Criando o grafo
grafo = nx.Graph()

# Inserindo os nodos
grafo.add_nodes_from([i+1 for i in range(N)])

# Inserindo as conexoes entre os nodos
for i in range(N):
    for j in range(0, i):
        if matrizAdj[i][j] == 1:
            grafo.add_edge(i+1, j+1)
                                                
# Desenhando o grafo
nx.draw_circular(grafo, with_labels=True, node_color="red")

# Plotando o grafo
plt.plot()

plt.axis('off')
plt.show()
