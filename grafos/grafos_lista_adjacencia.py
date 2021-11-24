
'''
Estrututa de grafos como lista de adjacência
Usaremos um dicionário:
Ex:
A -> [B, C]
B -> [C]
C -> [A]
'''
grafo1 = {
    "A": ["B","C"],
    "B": ["C"],
    "C": ["A"]
}

def sao_vizinhos(grafo, v1, v2):
    '''
    Função que retorna true se existe uma aresta que sai de v1 e entra em v2,
    e false caso contrário
    '''
    adjacentes_out = grafo[v1]
    for v in adjacentes_out:
        if v == v2:
            return True
    return False

    # return v2 in grafo[v1]  # v2 está na lista de adjacencia do v1
    
### teste:
assert sao_vizinhos(grafo1, "A", "C") == True
assert sao_vizinhos(grafo1, "B", "A") == False


def tem_aresta_entre(grafo, v1, v2):
    '''
    Responde true se tem uma aresta (em qualquer direção) entre v1 e v2
    '''
    return sao_vizinhos(grafo, v1, v2) or sao_vizinhos(grafo, v2, v1)

assert tem_aresta_entre(grafo1, "A", "C") == True
assert tem_aresta_entre(grafo1, "B", "A") == True


def vizinhanca(grafo, v1) -> list:
    return grafo[v1]


def busca_profundidade(grafo, v_inicial, chave):
    '''
    Função wrapper (pontapé inicial)
    '''
    return busca_profundidade_rec(grafo, v_inicial, chave, visitados=[])


def busca_profundidade_rec(grafo, v_inicial, chave, visitados):

    if v_inicial == chave:
        return True

    visitados.append(v_inicial)

    vizinhos = vizinhanca(grafo, v_inicial)

    for v_proximo in vizinhos:
        if v_proximo not in visitados:
            resultado = busca_profundidade_rec(grafo, v_proximo, chave, visitados)
            if resultado:
                return True

    return False


assert busca_profundidade(grafo1, "C", "B") == True
assert busca_profundidade(grafo1, "C", "D") == False       


def busca_largura(grafo, v_inicial, chave):
    pass


def existe_caminho_entre(grafo, v1, v2):
    pass

def eh_conexo(grafo):
    pass

'''
Estrututa de grafos *ponderados* como lista de adjacência
Usaremos um dicionário:
Ex:
A -> [(B,20),(C,60)] #significado: aresta entre A e B tem peso 20, e aresta entre A e C tem peso 60
B -> [(C,60)]
C -> [(A,15)]
'''
grafo2 = {
    "A": [("B",20), ("C",60)],
    "B": [("C",15)],
    "C": [("A",60)]
}


vertices_ligados_a_A = grafo2["A"]
primeira_aresta = vertices_ligados_a_A[0]
vertice_da_primeira_aresta = primeira_aresta[0]
peso_da_primeira_aresta = primeira_aresta[1]
print(vertice_da_primeira_aresta)
print(peso_da_primeira_aresta)

def menor_caminho_entre(grafo, v1, v2):
    pass