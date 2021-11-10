
"""
DICIONÁRIOS / MAPAS ASSOCIATIVOS / MAPAS CHAVE-VALOR



"""


"""
vetor (array):
lista_de_compras

chave (indice) -> valor
0 -> arroz
1 -> feijão
2 -> macarrão
....
9 -> carne

"""

n = 10
lista_de_compras = [None]*n

lista_de_compras[0] = "arroz"
lista_de_compras[1] = "feijao"
lista_de_compras[2] = "macarrão"
lista_de_compras[9] = "carne"

"""
Obs: ACESSO DIRETO A UMA POSIÇÃO NO VETOR:
lista_de_compras -> 32456  ## endereço de memória 

Acesso:
lista_de_compras[2] -> 32456 + 2 = 32458  ## O(1)
"""
# print(hash(lista_de_compras))

# print(list(range(len(lista_de_compras))))
# print(lista_de_compras)



"""
QUERO ARMAZENAR PESSOAS PELO CPF
????
tabela_pessoas_por_cpf

chave (indice) -> valor
CPF            -> nome

00001 -> "Maria Costa"
12345 -> "João da Silva"
82930 -> "Fulano de Souza"
....
99999 -> "Ciclano Oliveira"

"""

tabela_pessoas_por_cpf = dict()

tabela_pessoas_por_cpf[12345] = "João da Silva"  # Inserção: O(1)
tabela_pessoas_por_cpf[82930] = "Fulano de Souza"

print(tabela_pessoas_por_cpf)

print("A pessoa com CPF 82930 é:", tabela_pessoas_por_cpf[82930]) # Acesso/busca: O(1)

import random
import names
from pprint import pprint

tabela_pessoas_por_cpf = dict()  #CRIAÇÃO DE DICIONARIO VAZIO

quant = 1000

for i in range(100):
    cpf_aleatorio = random.randrange(0,100000)
    nome_aleatorio = names.get_full_name()
    tabela_pessoas_por_cpf[cpf_aleatorio] = nome_aleatorio #INSERÇÃO DE DADO NO DICIONARIO

pprint(tabela_pessoas_por_cpf)

print(tabela_pessoas_por_cpf.keys())

cpf_busca = random.choice(list(tabela_pessoas_por_cpf.keys()))

print("A pessoa que tem CPF "+str(cpf_busca)+" é:", tabela_pessoas_por_cpf[cpf_busca])


#### Dicionário de capitais

capitais_paises = dict()

#INSERÇÕES:
capitais_paises["Brasil"] = "Brasília"
capitais_paises["Argentina"] = "Buenos Aires"
capitais_paises["Uruguai"] = "Montevideo"

#ACESSOS:
#quero saber qual a capitaç do Uruguai:

print(capitais_paises["Uruguai"])  # O(1)
print(capitais_paises["Argentina"]) # O(1)