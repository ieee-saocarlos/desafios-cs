'''
Leite 	        12 	78
Ovo 	        12 	68
Prendedores 	24 	21
Sabão 	        5 	13
Iogurte 	    6 	40
'''
c_leite = 12,
c_ovo = 12,
c_prend = 24,
c_sabão = 5,
c_iogurte = 6

leite = input("Conjuntos de Leite")
ovo = input("Conjuntos de Ovo")
prend = input("Conjuntos de Prendedores")
sabao = input("Conjuntos de Sabão")
iogur = input("Conjuntos de Iogurte")


print("Há {} caixas de leite, {} ovos, {} prendedores, {} barras de sabão e {} copinhos de iogurte".format(\
    leite*c_leite,\
    ovo*c_ovo,\
    prend*c_prend,\
    sabao*c_sabão,\
    iogur*c_iogurte))
