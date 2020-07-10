# Unidades de cada conjunto
conj_leite = 12
conj_ovo = 12
conj_prendedores = 24
conj_sabao = 5
conj_iogurte = 6

# Quantidade de conjuntos
qtd_conj_leite = int(input("Quantidade de conjuntos de leite: "))
qtd_conj_ovo = int(input("Quantidade de conjuntos de ovo: "))
qtd_conj_prendedores = int(input("Quantidade de conjuntos de prendedores: "))
qtd_conj_sabao = int(input("Quantidade de conjuntos de sabão: "))
qtd_conj_iogurte = int(input("Quantidade de conjuntos de iogurte: "))

# Total de unidades de cada produto
leite = conj_leite * qtd_conj_leite
ovo = conj_ovo * qtd_conj_ovo
prendedores = conj_prendedores * qtd_conj_prendedores
sabao = conj_sabao * qtd_conj_sabao
iogurte = conj_iogurte * qtd_conj_iogurte

# Mostrando resultados
print("Há {0} caixas de leite, {1} ovos, {2} prendedores, {3} barras de sabão e {4} copinhos de iogurte.".format( leite, ovo, prendedores, sabao, iogurte))

