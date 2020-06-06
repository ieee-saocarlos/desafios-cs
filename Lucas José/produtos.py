milk = 12*int(input("Insira a quantide de conjuntos de leite: "))
egg = 12*int(input("\rInsira a quantide de conjuntos de ovos: "))
cpin = 24*int(input("\rInsira a quantide de conjuntos de prendedores: "))
soap = 5*int(input("\rInsira a quantide de conjuntos de sabão: "))
yogurt = 6*int(input("\rInsira a quantide de conjuntos de iogurte: "))

print("\n\rEstoque em unidades")
print("\r{0}: {1:d}".format("leite", milk))
print("\r{0}: {1:d}".format("ovos", egg))
print("\r{0}: {1:d}".format("prendedores", cpin))
print("\r{0}: {1:d}".format("barrinhas de sabão", soap))
print("\r{0}: {1:d}".format("copinhos de iogurte", yogurt))

input("\n\rPressione Enter para encerrar o programa")

