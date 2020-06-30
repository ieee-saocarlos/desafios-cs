"""
Código feito pela Ana Asano ao me ajudar a testar o desafio
"""

print("Olá vendedor Joaquim!")
print("Vamos começar!")

conj_leite = int(input("coloque a quantidade de conjuntos de leites"))
leite = conj_leite * 12

conj_ovo = int(input("coloque a quantidade de conjuntos de ovos"))
ovo = conj_ovo * 12

conj_prendedores = int(input("coloque a quantidade de conjuntos de prendedores"))
prendedor = conj_prendedores * 24

conj_sabao = int(input("coloque a quantidade de conjuntos de sabões"))
sabao = conj_sabao * 5

conj_iogurte = int(input("coloque a quantidade de conjuntos de iogurte"))
iogurte = conj_iogurte * 6

print("Há {0} caixas de leite, {1} ovos, {2} prendedores, {3} barras de sabão e {4} copinhos de iogurte"
      .format(leite, ovo, prendedor, sabao, iogurte))
