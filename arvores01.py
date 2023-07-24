import networkx as nx
#classes e funções para plotagem de grafico
import matplotlib.pyplot as plt
#cria grafo vazio
G = nx.Graph()
#adiciona vertice
G.add_node("a")
G.add_node("b")
G.add_node("c")
G.add_node("d")
G.add_node("e")
#adiciona arestas
G.add_edge("a","b")
G.add_edge("b","c")
G.add_edge("b","d")
G.add_edge("c","d")
G.add_edge("d","e")
#lista os vertices
print("lista de vertice")
print(G.nodes())
#percorre o conjunto de vertice
print("percorrendo vertice")
for vertc in G.nodes():
    print(vertc)
#lista as arestas
print("lista arestas")
print(G.edges())
#percorrendo arestas
print("percorrendo arestas")
for arest in G.edges():
    print(arest)
#mostra lista de graus
print("lista grau G")
print(G.degree())
#grafo como lista de adjacencias
print(G["a"])
print(G["b"])
print(G["c"])
print(G["d"])
print(G["e"])
#obtem a matriz de adjacencias
print("matriz de adjacencia")
A = nx.adjacency_matrix(G)#retorma a matriz pra ecoomizar memoria
print(A.todense())#converte para matriz padrao
#plotando como imagem
plt.figure(1)
#SPRING
nx.draw_networkx(G, pos = nx.spring_layout(G), with_labels = True)
plt.show()