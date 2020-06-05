# Desafio 2: Segunda Tarefa

#Unidades no conjunto usando dicionário
unidades = {
	'leite': 12,
	'ovo': 12,
	'prendedores': 24, 
	'sabao': 5, 
	'iogurte': 6
	}

quantidades = {
	'leite': unidades['leite']*78,
	'ovos': unidades['ovo']*68,
	'prendedores': unidades['prendedores']*21, 
	'barras de sabão': unidades['sabao']*13, 
	'copinhos de iogurte': unidades['iogurte']*40
	}

print("Quantidade de unidades de produtos:")
for produto in quantidades:
	print(produto,":",quantidades[produto])



