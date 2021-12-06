

def frequencias_caracteres(string: str) -> dict:
    
    dicionario = dict()

    # for (int i=0; i < string.lenght; i++):
    for i in range(0, len(string)): # i=0, i=1, i=2,..., i = len(string)-1
        
        letra = string[i]
        ## se a letra não está no dicionario
        if letra not in dicionario.keys():
            dicionario[letra] = 1
        else:
            dicionario[letra] = dicionario[letra] + 1
    
    return dicionario


## Main

resultado1 = frequencias_caracteres("ABACAXI")

resultado2 = frequencias_caracteres("ABOBODA")
print(resultado1)
print(resultado2)

