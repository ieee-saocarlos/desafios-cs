# Desafio 2: Terceira Tarefa

print("____________________________________________\n")
print("CALCULADORA DE UNIDADES DOS PRODUTOS.")
print("____________________________________________\n")

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
	
print("____________________________________________\n")
print("Há {0:d} caixas de leite, {1:d} ovos, {2:d} prendedores, {3:d} barras de sabão e {4:d} copinhos de iogurte.".format(quantidades['leite'], quantidades['ovos'], quantidades['prendedores'], quantidades['barras de sabão'], quantidades['copinhos de iogurte']))
