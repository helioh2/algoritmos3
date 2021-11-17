import copy

LIVRE = None
APAGADO = False

class TabelaHash: ## Definição do tipo TabelaHash

    def __init__(self, m: int):
        self.m = m
        self.n = 0
        self.vetor = [None]*m

    def __getitem__(self, index):
        return self.vetor[index]

    def __setitem__(self, index, chave):
        self.vetor[index] = chave

    def __str__(self) -> str:
        return str(self.vetor)



def hash_index(chave, k: int, m: int):
    """
    Calcula o hash com passo (k)
    """
    return (hash(chave) + k) % m


def inserir(chave, tabela: TabelaHash):
    k = 0
    indice_hash = hash_index(chave, k, tabela.m)

    while tabela[indice_hash] != LIVRE:
        k += 1
        indice_hash = hash_index(chave, k, tabela.m)
 
    tabela[indice_hash] = chave
    tabela.n += 1

    ## Verificação do fator de carga:
    fator_carga = tabela.n / tabela.m

    if fator_carga > 0.5:
        redimensionar(tabela)
    

def redimensionar(tabela: TabelaHash) -> TabelaHash:

    tabela.m = tabela.m * 2
    tabela.n = 0
    vetor_copia = copy.copy(tabela.vetor)
    tabela.vetor = [None]*tabela.m ## ZERANDO A TABELA

    for item in vetor_copia:
        if item != LIVRE and item != APAGADO:
            inserir(item, tabela)

    return tabela
    ## Implementação alternativa (necessário mudar as inserções para tabela = inserir(chave, tabela) )
    # nova_tabela = TabelaHash(tabela.m * 2)

    # for item in tabela:
    #     if item != LIVRE and item != APAGADO:
    #         tabela = inserir(item, nova_tabela)
    
    # return nova_tabela



def busca(chave, tabela: TabelaHash):
    k = 0
    indice_hash = hash_index(chave, k, tabela.m)
    h_inicial = indice_hash

    while tabela[indice_hash] != LIVRE:

        if tabela[indice_hash] == chave:
            return indice_hash  # Encontrou!!

        k += 1
        indice_hash = hash_index(chave, k, tabela.m)
        
        if indice_hash == h_inicial: ## Deu a volta!
            return -1
        
    return -1 ## Não encontrou!! 


def remover(chave, tabela: TabelaHash):

    indice_hash = busca(chave, tabela)
    
    if indice_hash == -1:
        return -1 # Não existe a chave
    
    tabela[indice_hash] = APAGADO
    tabela.n -= 1
    


##MAIN
tabela = TabelaHash(m=10)  ## None = Espaço Livre

print(tabela.m)
print(tabela.n)

inserir(5, tabela)
print(tabela.n)
inserir(7, tabela)
inserir(15, tabela)
inserir(25, tabela)
inserir(27, tabela)

print("Tabela antes do primeiro redimensionamento:\n\t", tabela)

inserir(8, tabela)

print("Tabela após o primeiro redimensionamento:\n\t", tabela)
print(tabela.n)

inserir(12, tabela)
inserir(19, tabela)
inserir(76, tabela)
inserir(89, tabela)

remover(25, tabela)

print("Tabela antes do segundo redimensionamento:\n\t", tabela)

inserir(92, tabela)
inserir(107, tabela)

print("Tabela após o segundo redimensionamento:\n\t", tabela)

print(busca(35, tabela))
print(busca(27, tabela))
print(busca(7, tabela))