
'''
Estrututa de grafos como matriz de adjacência]
Usaremos 'None' para marcar inexistência de aresta e '1' para marcar existência de aresta
Necessário definir um vetor auxiliar (chaves) para mapear o valor da chave referente
a cada linha/coluna
'''
grafo1 = [
    [None,1,1],
    [None,None,1],
    [1,None,None]
]
chaves = [1,2,3]  # 0 -> 1; 1 -> 2; 2 -> 3