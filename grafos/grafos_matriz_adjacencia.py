
'''
Estrututa de grafos como matriz de adjacência]
Usaremos 'None' para marcar inexistência de aresta e '1' para marcar existência de aresta
Necessário definir um vetor auxiliar (chaves) para mapear o valor da chave referente
a cada linha/coluna
'''
from typing import Tuple


class Grafo:

    def __init__(self, vertices:list, arestas:Tuple[object,object,int]) -> None:
        self.vertices = sorted(vertices)
        self.matriz = [[None for _ in range(len(vertices))] for _ in range(len(vertices))]
        
        for v1, v2, peso in arestas:
            i, j = vertices.index(v1), vertices.index(v2)
            self.matriz[i][j] = peso


vertices = ["A","B","C"]
arestas = [("A","B",1), ("A","C",1), ("B","C",1), ("C","A",1)]

grafo1 = Grafo(vertices, arestas)

print(grafo1.matriz)
