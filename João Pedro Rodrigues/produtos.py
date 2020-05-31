a = 'Digite as unidades do conjunto de '
b = 'Digite a quantidade de conjuntos de '

leite = int(input(a + 'leite: '))
leitec = int(input(b + 'leite: '))

ovos = int(input(a + 'ovos: '))
ovosc = int(input(b + 'ovos: '))

prend = int(input(a + 'prendedores: '))
prendc = int(input(b + 'prendedores: '))

sabao = int(input(a + 'sabao: '))
sabaoc = int(input(b + 'sabao: '))

iog = int(input(a + 'iogurte: '))
iogc = int(input(b + 'iogurte: '))

leite = leite * leitec
ovos = ovos * ovosc
prend = prend * prendc
sabao = sabao * sabaoc
iog = iog * iogc

print("Há {0} caixas de leite, {1} ovos, {2} prendedores, {3} barras de sabão e {4} copinhos de iogurte".format(leite, ovos, prend, sabao, iog))


