"""
Implementação do Heap Mínimo
"""

def menor_elemento(lista):
    return lista[1]

def filho_esquerda(lista, i):
    return lista[2 * i]

def filho_direita(lista, i):
    return lista[2 * i + 1]

def pai(lista, i):
    return lista[i // 2]

def inserir_heap(lista, item):
    lista.append(item) # adiciona no final da lista
    promove(lista, len(lista)-1)
    return lista

def remover_primeiro_heap(lista):
    ind_ultimo = len(lista) - 1
    ind_primeiro = 1
    lista[ind_primeiro], lista[ind_ultimo] = lista[ind_ultimo], lista[ind_primeiro]
    item = lista.pop()  # remove ultimo (que era o primeiro)
    demove(lista)
    return item

def eh_heap_min(lista):
    for i in range(2, len(lista)):
        if lista[i] < lista[i // 2]:
            return False
    return True

def promove(lista, n): # também chamado de 'heapify'
    """
    Heapify, onde n é o último elemento a ser considerado.
    """
    i = n

    while True:
        # Elemento chegou na raiz da árvore.
        if i == 1:
            break

        # Elemento chegou na posição correta.
        p = i // 2
        if lista[p] <= lista[i]:
            break

        # Senão: Troca elemento de lugar com o pai.
        lista[p], lista[i] = lista[i], lista[p]

        i = p

    return lista


def demove(lista):
    i = 1
    ind_ultimo = len(lista) - 1

    while True:
        ind_filho_esq = 2 * i
        ind_filho_dir = 2 * i + 1
        ind_filho_menor = ind_filho_esq

        # Elemento não tem mais filhos.
        if ind_filho_esq > ind_ultimo:
            break

        # Encontra o índice do menor dos filhos.
        if ind_filho_dir <= ind_ultimo:
            if lista[ind_filho_dir] < lista[ind_filho_esq]:
                ind_filho_menor = ind_filho_dir

        # O elemento é menor que seu menor filho.
        if lista[i] <= lista[ind_filho_menor]:
            break

        # Troca elemento de lugar com o menor filho.
        lista[ind_filho_menor], lista[i] = lista[i], lista[ind_filho_menor]

        i = ind_filho_menor
    
    return lista

# Testes

lista1 = [None, 2, 4, 5, 9, 8, 6, 7, 1]
# lista1 = [None, 2, 4, 5, 1, 8, 6, 7, 9]
# lista1 = [None, 2, 1, 5, 4, 8, 6, 7, 9]
# lista1 = [None, 1, 2, 5, 4, 8, 6, 7, 9]
assert promove(lista1, len(lista1)-1) == [None, 1, 2, 5, 4, 8, 6, 7, 9]

inserir_heap(lista1, 3)
# [None, 1, 2, 5, 4, 8, 6, 7, 9]
# [None, 1, 2, 5, 4, 8, 6, 7, 9, 3]
# [None, 1, 2, 5, 3, 8, 6, 7, 9, 4]
print(lista1)

assert lista1 == [None, 1, 2, 5, 3, 8, 6, 7, 9, 4]

item = remover_primeiro_heap(lista1)
# [None, 1, 2, 5, 3, 8, 6, 7, 9, 4]
# [None, 4, 2, 5, 3, 8, 6, 7, 9, 1]
# [None, 4, 2, 5, 3, 8, 6, 7, 9]
# [None, 2, 4, 5, 3, 8, 6, 7, 9]
# [None, 2, 3, 5, 4, 8, 6, 7, 9]

print(lista1)
assert lista1 == [None, 2, 3, 5, 4, 8, 6, 7, 9]
assert item == 1
