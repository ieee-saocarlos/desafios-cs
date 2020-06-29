# Frase inicial
print("Calculadora de quantidade de produtos \n")

# Tamanho dos conjuntos
# Separei dessa forma para facilitar a modificação caso o tamanho de um conjunto mude
milk_pack = 12   # Pacote de caixas de leite
egg_pack = 12    # Cartela de ovos
peg_pack = 24    # Pacote de pregadores
soap_pack = 5    # Pacote de sabonetes
yogurt_pack = 6  # Conjunto de iogurtes

# Pede a quantidade de conjuntos e calcula o total de unidades
milk_qty = int(input("Insira a quantidade de pacotes de LEITE: ")) * milk_pack
egg_qty = int(input("Insira a quantidade de cartelas de OVOS: ")) * egg_pack
peg_qty = int(input("Insira a quantidade de pacotes de PRENDEDOR: ")) * peg_pack
soap_qty = int(input("Insira a quantidade de pacotes de SABÃO: ")) * soap_pack
yogurt_qty = int(input("Insira a quantidade de conjuntos de IOGURTE: ")) * yogurt_pack

print('''Há \
{0} caixas de leite, \
{1} ovos, \
{2} prendedores, \
{3} barras de sabão e \
{4} copinhos de iogurte.'''
      .format(milk_qty, egg_qty, peg_qty, soap_qty, yogurt_qty))
