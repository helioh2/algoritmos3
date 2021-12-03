
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


def busca_profundidade_rec_template(grafo, v_inicial, visitados):

    # faz algo com v_inicial

    visitados.append(v_inicial)

    vizinhos = vizinhanca(grafo, v_inicial)

    for v_proximo in vizinhos:
        if v_proximo not in visitados:
            resultado = busca_profundidade_rec_template(grafo, v_proximo, visitados)
            # faz algo com resultado do vizinho



def busca_profundidade_nao_rec_pilha(grafo, v_inicial):
    visitados = set()  #conjunto
    pilha = [v_inicial]

    while pilha: ## enquanto pilha não está vazia
        vertice = pilha.pop(-1)  #remove último (desempilhando)

        # faz alguma coisa com vertice (ex: verifica se é o que está procurando)

        if vertice not in visitados:
            visitados.add(vertice)
            vizinhos_nao_visitados = [v for v in vizinhanca(grafo, vertice) if v not in visitados]
            pilha += vizinhos_nao_visitados #acrescenta vizinhos não visitados ao topo da pilha

    return visitados

grafo_aciclico = {
    "A": ["B","C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["G"],
    "E": ["F"],
    "F": [],
    "G": []
}


print(busca_profundidade_nao_rec_pilha(grafo_aciclico, "A"))  


def ordenacao_topologica(grafo):
    """
    DFS (busca em profundidade) modificada para retornar a ordenação topológica do grafo.
    Isso é feito por meio da lista com os tempos de término do processamento
    de cada vértice, que será a ordenação topológica reversa do grafo.
    """

    visitados = set()
    ordem_topologica = {v: 0 for v in grafo.keys()}
    tempo = 0

    def busca_profundidade(grafo, v_inicial, visitados):

        visitados.add(v_inicial)
        vizinhos = vizinhanca(grafo, v_inicial)

        for v_proximo in vizinhos:
            if v_proximo not in visitados:
                busca_profundidade(grafo, v_proximo, visitados)

        nonlocal tempo
        tempo += 1
        
        ordem_topologica[v_inicial] = tempo


    for vertice in grafo:
        if not vertice in visitados:
            busca_profundidade(grafo, vertice, visitados)

    return {v: abs(t-len(grafo)) for v,t in ordem_topologica.items()} # reverte ordem

grafo_aciclico = {
    "A": ["B","C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["G"],
    "E": ["F"],
    "F": [],
    "G": []
}

print(ordenacao_topologica(grafo_aciclico))


def busca_largura_nao_rec_fila(grafo, v_inicial):
    visitados = set()  #conjunto
    fila = [v_inicial]

    while fila: ## enquanto pilha não está vazia
        vertice = fila.pop(0)  #remove primeiro (início da fila)

        if vertice not in visitados:

            print(vertice, end=", ")

            visitados.add(vertice)
            vizinhos_nao_visitados = [v for v in vizinhanca(grafo, vertice) if v not in visitados]
            fila += vizinhos_nao_visitados #acrescenta vizinhos não visitados ao topo da pilha

    return visitados

print("Execução da busca em largura:")
busca_largura_nao_rec_fila(grafo_aciclico, "A")


def dikjstra(grafo, v_inicial):
    visitados, fila = [], [v_inicial]

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)
            fila += [x for x in grafo[vertice] if x not in visitados]
    return visitados

# print(busca_largura(grafo1, "C"))


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