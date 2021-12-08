

from typing import Set


class Trie:

    def __init__(self, chave:str=None, filhos:Set=None):
        self.chave = chave
        if not filhos:
            self.filhos = set()
        else:
            self.filhos = filhos

    def inserir_string(self, string:str):

        if not string:
            return

        for filho in self.filhos:
            if filho.chave == string[0]:
                filho.inserir_string(string[1:])
                return

        #else
        novo_filho = Trie(string[0])
        self.filhos.add(novo_filho)
        novo_filho.inserir_string(string[1:])
        
    def busca_string(self, string:str) -> bool:
        
        if not string:
            return True

        if not self.chave or string[0] == self.chave:

            substring = string[1:] if self.chave else string

            if not self.filhos and len(string) == 1: # nó folha e último caractere == encontrou string 
                return True

            for filho in self.filhos:
                achou_filho = filho.busca_string(substring)
                if achou_filho:
                    return achou_filho
            #else
            return False

        #else
        return False

    def __str__(self) -> str:

        def to_str_rec(trie, nivel):
            chave_str = trie.chave if trie.chave else "*"
            string = nivel*"\t" + chave_str + "\n"
            for filho in trie.filhos:
                string +=  to_str_rec(filho, nivel+1)
            return string
        
        return to_str_rec(self, nivel=0)

       

trie = Trie()  #trie vazio
trie.inserir_string("o")
trie.inserir_string("rato")
trie.inserir_string("roeu")
trie.inserir_string("a")
trie.inserir_string("roupa")
trie.inserir_string("do")
trie.inserir_string("rei")
trie.inserir_string("de")
trie.inserir_string("roma")

print(trie)

assert trie.busca_string("rato")
assert not trie.busca_string("ratol")
assert trie.busca_string("")
assert trie.busca_string("o")
