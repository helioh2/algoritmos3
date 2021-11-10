
M = 10

tabela_hash = [[] for _ in range(M)]  #Lista de listas

print(tabela_hash)
print(tabela_hash[2])


def hash_index(chave):
    """
    "cafe" -> hash("cafe") % M

    """
    return hash(chave) % M

def inserir(chave, tabela_hash):
    indice_hash = hash_index(chave)
    # tabela_hash[indice_hash]  #é uma lista
    tabela_hash[indice_hash].append(chave)

def contem(chave, tabela_hash):
    indice_hash = hash_index(chave)
    # tabela_hash[indice_hash]  #é uma lista
    
    for item in tabela_hash[indice_hash]:
        if item == chave:
            return True

    return False


def remover(chave, tabela_hash):
    indice_hash = hash_index(chave)
    # tabela_hash[indice_hash]  #é uma lista
    if chave in tabela_hash[indice_hash]:
        tabela_hash[indice_hash].remove(chave)



print(hash("cafe"))
print(hash("macarrao"))

inserir("cafe", tabela_hash)
inserir("macarrao", tabela_hash)
inserir("arroz", tabela_hash)
inserir("cha", tabela_hash)
inserir("carne", tabela_hash)
inserir("repolho", tabela_hash)
inserir("detergente", tabela_hash)

print(tabela_hash)



def print_tabela_hash(tabela_hash):

    for i in range(M):
        print(i, "-->", tabela_hash[i])


print_tabela_hash(tabela_hash)

print("Arroz está na tabela?", contem("arroz", tabela_hash))  # True
print("Arroz está na tabela?", contem("frango", tabela_hash)) # False

remover("carne", tabela_hash)

print("Após remoção:")
print_tabela_hash(tabela_hash)
