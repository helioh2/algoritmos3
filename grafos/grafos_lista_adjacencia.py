
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
    '''
    Ex ordem_topologica
    A -> 0
    B -> 0
    C -> 0
    D -> 0
    E -> 0
    F -> 0
    G -> 0
    '''
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
    ## se os vertices fossem numeros de 0..len(grafo) e ordem_topologica fosse uma lista
    ## return ordem_topologica.reverted
    

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


def busca_menor_distancia_e_nao_visitado(grafo, distancia, visitado):

    menor = None
    primeiro = True
    for v in grafo:
        if distancia[v] >= 0 and not visitado[v]:
            if primeiro:
                menor = v
                primeiro = False
            elif distancia[menor] > distancia[v]:
                menor = v
    return menor


INF = float('inf')

def menor_caminho(grafo, v_inicial):

    visitado = {v: False for v in grafo} # cria relação de visitado (True ou False) para cada vértice
    cont_nao_visitados = len(grafo.keys()) # contagem de não visitados inicialmente como número total de vértices
    distancia = {v: INF for v in grafo} # cria relação de distância inicial (INF) para cada vértice
    anterior = {v: None for v in grafo} # cria relação de anterior inicial (None) para cada vértice
    
    distancia[v_inicial] = 0

    while cont_nao_visitados > 0:

        menor_v = busca_menor_distancia_e_nao_visitado(grafo, distancia, visitado)

        if menor_v is None:
            break

        visitado[menor_v] = True
        cont_nao_visitados -= 1

        for vizinho in vizinhanca(grafo, menor_v):  # para cada vizinho do menor
            if (distancia[menor_v] + 1 < distancia[vizinho]): 
                # Se ninguém chegou ainda no vizinho ou a distância do vizinho 
                # é maior que a distancia do menor_v incrementado
                # Ou peso da aresta:
                # elif  distancia[vizinho] > distancia[menor_v] + peso(menor_v, vizinho):   
                
                distancia[vizinho] = distancia[menor_v] + 1
                # ou peso da aresta: 
                # distancia[vizinho] = distancia[menor_v] + peso(menor_v, vizinho)
                anterior[vizinho] = menor_v

    return distancia, anterior

print("\nTestes menor caminho:")
grafo_com_pesos = {
    0: [1],
    1: [2, 3],
    2: [4],
    3: [0, 5],
    4: [1],
    5: []
}

# print(menor_caminho(grafo1, "A"))
print(menor_caminho(grafo_com_pesos, 0))


'''
Estrututa de grafos *ponderados* como lista de adjacência
Usaremos um dicionário:
Ex:
A -> [(B,20),(C,60)] #significado: aresta entre A e B tem peso 20, e aresta entre A e C tem peso 60
B -> [(C,60)]
C -> [(A,15)]
'''
grafo_com_pesos = {
    "A": [("B",20), ("C",60)],
    "B": [("C",15)],
    "C": [("A",60)]
}

def peso(grafo, v1, v2):
    
    for i in range(len(grafo[v1])):
        if grafo[v1][i][0] == v2: #achei a aresta entre v1 e v2
            return grafo[v1][i][1]
    return None

assert peso(grafo_com_pesos, "A", "C") == 60
assert peso(grafo_com_pesos, "B", "C") == 15

      

INF = float('inf')

def vizinhanca_ponderada(grafo, v1):
    # result = []
    # for item in grafo[v1]:
    #     result.append(item[0])
    # return result
    return [v for (v,p) in grafo[v1]]


def menor_caminho_com_pesos(grafo, v_inicial):  ## Algoritmo de Dijkstra

    visitado = {v: False for v in grafo} # cria relação de visitado (True ou False) para cada vértice
    cont_nao_visitados = len(grafo.keys()) # contagem de não visitados inicialmente como número total de vértices
    distancia = {v: INF for v in grafo} # cria relação de distância inicial (INF) para cada vértice

    anterior = {v: None for v in grafo} # cria relação de anterior inicial (None) para cada vértice
    
    distancia[v_inicial] = 0

    while cont_nao_visitados > 0:

        menor_v = busca_menor_distancia_e_nao_visitado(grafo, distancia, visitado)

        if menor_v is None:
            break

        visitado[menor_v] = True
        cont_nao_visitados -= 1

        for vizinho in vizinhanca_ponderada(grafo, menor_v):  # para cada vizinho do menor
            if (distancia[menor_v] + peso(grafo, menor_v, vizinho) < distancia[vizinho]): 
                # Se ninguém chegou ainda no vizinho ou a distância do vizinho 
                # é maior que a distancia do menor_v incrementado
                # Ou peso da aresta:
                # elif  distancia[vizinho] > distancia[menor_v] + peso(menor_v, vizinho):   
                
                distancia[vizinho] = distancia[menor_v] + peso(grafo, menor_v, vizinho)
                # ou peso da aresta: 
                # distancia[vizinho] = distancia[menor_v] + peso(menor_v, vizinho)
                anterior[vizinho] = menor_v

    return distancia, anterior


print(vizinhanca_ponderada(grafo_com_pesos, "A"))

print(menor_caminho_com_pesos(grafo_com_pesos, "A"))

# vertices_ligados_a_A = grafo2["A"]
# primeira_aresta = vertices_ligados_a_A[0]
# vertice_da_primeira_aresta = primeira_aresta[0]
# peso_da_primeira_aresta = primeira_aresta[1]
# print(vertice_da_primeira_aresta)
# print(peso_da_primeira_aresta)
