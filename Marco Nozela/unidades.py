# Desafio 2: Segunda Tarefa

print("Calculadora de unidades dos produtos.\n")

#Unidades no conjunto usando dicionário
unidades = {
	'leite': 12,
	'ovo': 12,
	'prendedores': 24, 
	'sabao': 5, 
	'iogurte': 6
	}

quantidades = {
	'leite': unidades['leite']*int(input("Digite quantos conjuntos de leite.\n")),
	'ovos': unidades['ovo']*int(input("Digite quantos conjuntos de ovo.\n")),
	'prendedores': unidades['prendedores']*int(input("Digite quantos conjuntos de prendedores.\n")), 
	'barras de sabão': unidades['sabao']*int(input("Digite quantos conjuntos de sabão.\n")), 
	'copinhos de iogurte': unidades['iogurte']*int(input("Digite quantos conjuntos de iogurte.\n"))
	}

print("\nQuantidade de unidades de produtos:")
for produto in quantidades:
	print(produto,":",quantidades[produto])



