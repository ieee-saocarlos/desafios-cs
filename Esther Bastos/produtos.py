leite = int(input("Número de conjuntos de leite: "))
ovo = int(input("Número de conjuntos de ovo: "))
prendedores = int(input("Número de conjuntos de prendedores: "))
sabão = int(input("Número de conjuntos de sabão: "))
iogurte = int(input("Número de conjuntos de iogurte: "))

leite = 12 * leite
ovo = 12 * ovo
prendedores = 24 * prendedores
sabão = 5 * sabão
iogurte = 6 * iogurte

print("Há {0} caixas de leite, {1} ovos, {2} prendedores, {3} barras de sabão e {4} copinhos de iogurte".format(leite, ovo, prendedores, sabão, iogurte))