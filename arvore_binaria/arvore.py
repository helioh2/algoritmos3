from pprint import pprint

ARVORE_VAZIA = None

class Node:
    def __init__(self, conteudo, esq=None, dir=None):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        if self.conteudo != other.conteudo:
            return False 
        return self.esq == other.esq and self.dir == other.dir
        

###FUNÇÕES AUXILIARES:
def print_node(node):
    pprint(node.__dict__)

def constroi_arvore_predefinida(tupla: tuple):

    def constroi_arvore_from_indice_tupla(tupla, indice):
        if indice >= len(tupla):
            return None
        return constroi_arvore_predefinida(tupla[indice])

    if len(tupla) == 0:
        return Node()

    return Node(tupla[0], 
                constroi_arvore_from_indice_tupla(tupla, 1),
                constroi_arvore_from_indice_tupla(tupla, 2)
                )


###Funções de operações:

def adiciona(raiz: Node, elemento) -> Node:
    """
    Recebe uma árvore e um elemento, e adiciona o elemento na árvore.
    """
    if raiz == ARVORE_VAZIA:  ## CASO BASE
        return Node(elemento)

    if elemento < raiz.conteudo:
        nova_subarvore_esq = adiciona(raiz.esq, elemento)
        raiz.esq = nova_subarvore_esq
    else:
        nova_subarvore_dir = adiciona(raiz.dir, elemento)
        raiz.dir = nova_subarvore_dir
    
    return raiz


##TESTES:
assert adiciona(None, 50) == Node(50)
arvore_dois_nodes = Node(50, Node(20), None)
assert adiciona(Node(50), 20) == arvore_dois_nodes
arvore_tres_nodes = Node(50, Node(20), Node(70))
assert adiciona(arvore_dois_nodes, 70) == arvore_tres_nodes

arvore4 = Node(50, Node(20, None, Node(30)), Node(70))
arvore5 = Node(50, Node(20, None, Node(30, Node(25), None)), Node(70))
assert adiciona(arvore_tres_nodes, 30) == arvore4
assert adiciona(arvore4, 25) == arvore5

### MAIN
arvore_vazia = None  ##Null

arvore_com_um_elemento = Node(50)
# print_node(arvore_com_um_elemento)

subarvore_esquerda = Node(20)
subarvore_direita = Node(70)
arvore_com_tres_elementos_balanceada = Node(50, subarvore_esquerda, subarvore_direita)
# arvore_com_tres_elementos_balanceada = Node(50, Node(20), Node(70))
# print_node(arvore_com_tres_elementos_balanceada)
# print_node(arvore_com_tres_elementos_balanceada.esq)
# print_node(arvore_com_tres_elementos_balanceada.dir)

arvore_tupla1 = ("macarrao", 
                    ("feijao", ("arroz",), ("jujuba",)), 
                    ("patê", ("ovos",), ("salsicha",))
                )

arvore_teste = constroi_arvore_predefinida(arvore_tupla1)
