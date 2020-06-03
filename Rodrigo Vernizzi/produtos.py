L = 12
O = 12
P = 24
S = 5
I = 6

leite = int(input("Digite a quantidade de Leite:"))
ovo = int(input("Digite a quantidade de Ovo:"))
prendedor = int(input("Digite a quantidade de Prendedor:"))
sabao = int(input("Digite a quantidade de Sabão:"))
iogurte = int(input("Digite a quantidade de Iogurte:"))

v = L*leite
w = O*ovo
x = P*prendedor
y = S*sabao
z = I*iogurte


print("Há {} caixas de leite, {} ovos, {} prendedores, {} barras de sabão e {} copinhos de iogurte.".format(v, w, x, y, z))
