


def busca_sequencial(lista, valor):
    n = len(lista)        # O(1)
    for i in range(0, n):  # 1 = O(1)
        if lista[i] == valor:  # O(1)
            return i    # O(1)
    return -1  # 0

assert busca_sequencial([2,4,6,8],2) == 0  # lista[0] == 2

# Melhor caso: O(1) + O(1) + O(1) + O(1) + 0 = O(1)




## Função testada:
def busca_sequencial(lista, valor):
    n = len(lista)        # O(1)
    for i in range(0, n):  # n+1 = O(n)
        if lista[i] == valor:  # O(n)
            return i    # 0
    return -1  # O(1)

# Pior caso: O(1) + O(n) + O(n) +  O(1) = O(n)



## Função testada:
def busca_sequencial(lista, valor):
    n = len(lista)        # O(1)
    for i in range(0, n):  # n*(1/2) = O(n)
        if lista[i] == valor:  # O(n)
            return i    # O(1)
    return -1  # 0

# Caso médio: O(1) + O(n) + O(n) +  O(1) = O(n)
