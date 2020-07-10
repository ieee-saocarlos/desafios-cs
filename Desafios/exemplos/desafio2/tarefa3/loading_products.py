"""
Programa feito em homenagem ao Loli para dar um exemplo de barra de carregamento.
"""

import time

# Saudação ao usuário
print("oie \n")

# Tamanho dos conjuntos
milk_pack = 12
egg_pack = 12
peg_pack = 24
soap_pack = 5
yogurt_pack = 6

# Pede a quantidade de cada conjunto
milk_qty = int(input("Insira a quantidade de pacotes de LEITE: "))
egg_qty = int(input("Insira a quantidade de cartelas de OVOS: "))
peg_qty = int(input("Insira a quantidade de pacotes de PRENDEDOR: "))
soap_qty = int(input("Insira a quantidade de pacotes de SABÃO: "))
yogurt_qty = int(input("Insira a quantidade de conjuntos de IOGURTE: "))

# Calculando a quantidade de unidades
milk_un = milk_pack * milk_qty
time.sleep(1)
print("\n[#    ]")
egg_un = egg_pack * egg_qty
time.sleep(1)
print("[##   ]")
peg_un = peg_pack * peg_qty
time.sleep(1)
print("[###  ]")
soap_un = soap_pack * soap_qty
time.sleep(1)
print("[#### ]")
yogurt_un = yogurt_pack * yogurt_qty
time.sleep(1)
print("[#####]\n")

print('''Há \
{0} caixas de leite, \
{1} ovos, \
{2} prendedores, \
{3} barras de sabão e \
{4} copinhos de iogurte.'''
      .format(milk_un, egg_un, peg_un, soap_un, yogurt_un))
