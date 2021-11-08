from arvore import *

def contem(raiz: Node, elemento: object) -> bool:
    """
    Recebe a raiz de uma árvore e um elemento e responde se o elemento está ou não
    na árvore.
    """
    if raiz == None:
        return False
    
    if raiz.conteudo == elemento:  #ACHOU
        return True

    if elemento < raiz.conteudo:
        if contem(raiz.esq, elemento):
            return True       
    else:
        if contem(raiz.dir, elemento):
            return True

    return False



## TESTES
assert not contem(None, 20) #== False
assert contem(Node(20), 20) #== True
assert contem(Node(20), 30) == False

assert contem(Node(20, Node(10), Node(30)), 10)

arvore_prof_2 = Node(20, 
                        Node(15, 
                                Node(10), 
                                Node(18)
                            ), 
                        Node(30))
assert contem(arvore_prof_2, 10)



### METODOS DE PERCURSO (TRAVERSE)

def print_preordem(raiz: Node):

    print(raiz.conteudo)

    if raiz.esq:
        print_preordem(raiz.esq)
        
    if raiz.dir:
        print_preordem(raiz.dir)


def print_emordem(raiz: Node):
    if raiz.esq:
        print_emordem(raiz.esq)

    print(raiz.conteudo)

    if raiz.dir:
        print_emordem(raiz.dir)


def alguma_coisa_emordem(raiz: Node):
    if raiz.esq:
        alguma_coisa_emordem(raiz.esq)

    # VISITANDO
    alguma_coisa(raiz.conteudo)

    if raiz.dir:
        alguma_coisa_emordem(raiz.dir)






def multiplicar_por_dois_emordem(raiz: Node):
    
    if raiz.esq:
        multiplicar_por_dois_emordem(raiz.esq)

    raiz.conteudo = raiz.conteudo*2

    if raiz.dir:
        multiplicar_por_dois_emordem(raiz.dir)

        
def print_posordem(raiz: Node):
    if raiz.esq:
        print_posordem(raiz.esq)

    if raiz.dir:
        print_posordem(raiz.dir)

    print(raiz.conteudo)
    

arvore_exemplo = Node(18, 
                        Node(8, 
                                Node(4), 
                                Node(15)
                            ), 
                        Node(30,
                                Node(23),
                                Node(42)))

print("Pré-ordem:")
print_preordem(arvore_exemplo)
print("-------")
print("Em-ordem:")
print_emordem(arvore_exemplo)
print("-------")
print("Pós-ordem:")
print_posordem(arvore_exemplo)


def print_parenteses_preordem(raiz: Node):
    print("(", end="")

    print(raiz.conteudo, end="") 

    if raiz.esq:
        print_parenteses_preordem(raiz.esq) 

    if raiz.dir:     
        print_parenteses_preordem(raiz.dir)

    print(")", end="")
    

print("\nImpressão de notação em parênteses:")
print_parenteses_preordem(arvore_exemplo)


def print_parenteses_preordem_indentado(raiz: Node, nivel=0):
    print(nivel*"\t" + "(", end="")
    print(raiz.conteudo) 

    if raiz.esq:
        print_parenteses_preordem_indentado(raiz.esq, nivel+1) 

    if raiz.dir:     
        print_parenteses_preordem_indentado(raiz.dir, nivel+1)
        
    print(nivel*"\t" + ")")
    

print("\nImpressão de notação em parênteses:")
print_parenteses_preordem_indentado(arvore_exemplo)


def somatorio_arvore(raiz: Node) -> object:
    """
    Faz a soma de todos os elementos da árvore
    """
    if raiz is None:
        return 0

    soma = raiz.conteudo
    soma = soma + somatorio_arvore(raiz.esq)
    soma = soma + somatorio_arvore(raiz.dir)

    return soma

print(somatorio_arvore(arvore_exemplo))