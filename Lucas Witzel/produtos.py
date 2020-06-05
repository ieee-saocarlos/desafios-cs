print("Digite a quantidade de conjuntos de leite:")
leite=int(input())
print("Digite a quantidade de conjuntos de ovos:")
ovo=int(input())
print("Digite a quantidade de conjuntos de prendedores:")
prendedores=int(input())
print("Digite a quantidade de conjuntos de sabao:")
sabao=int(input())
print("Digite a quantidade de conjuntos de iogurte:")
iogurte=int(input())

l = 12 * leite
o = 12 * ovo
p = 24 * prendedores
s = 5 * sabao
i = 6 * iogurte

print("Há {0} caixas de leite, {1} ovos, {2} prendedores, {3} barras de sabão e {4} copinhos de iogurte".format(l,o,p,s,i))
