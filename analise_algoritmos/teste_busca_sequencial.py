from busca_sequencial import *


# print(busca_sequencial([4,8,15,16,23,42], 23))
# print(busca_sequencial([4,8,15,16,23,42], 44))
# print(busca_sequencial([4,8,15,16,23,42], 42))

# # TESTES AUTOMATIZADOS:
assert busca_sequencial([4,8,15,16,23,42], 23) == 4  # TESTE FUNCIONAL, OU CAIXA PRETA
assert busca_sequencial([4,8,15,16,23,42], 44) == -1
## Testes em valores limítrofes:
assert busca_sequencial([4,8,15,16,23,42], 42) == 5
assert busca_sequencial([4,8,15,16,23,42], 4) == 0
print("PARABÉNS!! TODOS OS TESTES PASSARAM")
        