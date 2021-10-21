import copy

from typing import Tuple
from arvore import *
from busca_arvore import *


def remover(raiz: Node, elemento) -> Node:
    
    ## Função auxiliar:
    def remover_e_retornar_sucessor(raiz_dir: Node) -> Tuple[Node,Node]:
        """
        Recebe o nó raiz (raiz_dir) referente à subárvore direita de raiz, e retorna o sucessor da subárvore raiz, se houver, e a
        subárvore direita modificada.
        """
        if raiz_dir == None:
            return None, raiz_dir

        anterior = atual = raiz_dir

        ## Desce na subárvore direita até chegar ao nó extremo esquerdo (este é o sucessor)
        while atual.esq != None:
            anterior = atual
            atual = atual.esq

        sucessor = atual

        ## Faz o pai do sucessor ter como subárvore esquerda a subárvore direita do sucessor
        anterior.esq = sucessor.dir

        return sucessor, raiz_dir
        
    ## -- Inicio do corpo da função 'remover']

    if raiz is None:
        return raiz

    if raiz.conteudo == elemento:
        node_sucessor, new_dir = remover_e_retornar_sucessor(raiz.dir)

        if node_sucessor is None:
            ## Se não tem sucessor, então o resultado é a própria subárvore esquerda
            return raiz.esq

        # Faz o sucessor apontar para a subárvore esquerda da raiz
        # e para a nova subárvore direita (que exclui o sucessor de sua posição anterior)
        node_sucessor.esq = raiz.esq
        node_sucessor.dir = new_dir

        # O sucessor passa a ser a nova raiz da árvore
        return node_sucessor

    return Node(raiz.conteudo, remover(raiz.esq, elemento), remover(raiz.dir, elemento))

    
arvore1 = Node(64, 
                    Node(30), 
                    Node(99,
                        Node(69,
                                None,
                                Node(78,
                                        None,
                                        Node(94))),
                        None))

arvore1_remove_64 = Node(69, 
                        Node(30), 
                        Node(99,                          
                            Node(78,
                                    None,
                                    Node(94)),
                            None))   

arvore1_copy = copy.deepcopy(arvore1)
result = remover(arvore1_copy, 64)
print_parenteses_preordem_indentado(result)
assert result == arvore1_remove_64           

arvore1_copy = copy.deepcopy(arvore1)
arvore2 = Node(150, arvore1_copy, None)
arvore2_remove_64 = Node(150, arvore1_remove_64, None) 

result = remover(arvore2, 64)
print_parenteses_preordem_indentado(result)
assert result == arvore2_remove_64

