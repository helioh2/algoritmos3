
def busca_sequencial(lista: list, valor: int) -> int:
    """
    Faz a busca pelo valor numa lista, retornando a posição do valor na lista
    ou -1 se não estiver na lista.
    
    List, Int -> Int[-1,n-1], onde n é o tamanho da lista
    """
    print(valor)
    n = len(lista)   # tamanho da lista
    for i in range(0, n):  # iteração sobre os índices: 0, 1, 2,..., n-1
        print(i)
        if lista[i] == valor:
            return i
    return -1
    
# print(busca_sequencial([4,8,15,16,23,42], 23))
# print(busca_sequencial([4,8,15,16,23,42], 44))
# print(busca_sequencial([4,8,15,16,23,42], 42))

# MAIN:

# # TESTES AUTOMATIZADOS:
assert busca_sequencial([4,8,15,16,23,42], 23) == 4  # TESTE FUNCIONAL, OU CAIXA PRETA
assert busca_sequencial([4,8,15,16,23,42], 44) == -1
## Testes em valores limítrofes:
assert busca_sequencial([4,8,15,16,23,42], 42) == 5
assert busca_sequencial([4,8,15,16,23,42], 4) == 0
print("PARABÉNS!! TODOS OS TESTES PASSARAM")
        



