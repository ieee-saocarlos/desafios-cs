# DESAFIO 2, TERCEIRA TAREFA
class Produto:
    """
    nome: nome do produto
    pacote: quantos produtos um pacote tem
    """
    def __init__(self, nome, pacote):
        self.nome = nome
        self.pacote = pacote
        self.conjuntos = 0
    
    def pergunta(self):
        #pede a entrada da quantidade de pacotes do produto atual
        self.conjuntos = int(input(
            (
            'Insira a quantidade de pacotes de {} e aperte ENTER: '
            ).format(self.nome)
            ))

    def resposta(self):
        # retorna a string com o total do produto atual
        return ('{} {}, ').format(self.conjuntos * self.pacote, self.nome)

produtos = [
    Produto('caixinhas de leite', 12),
    Produto('ovos', 12),
    Produto('prendedores', 24),
    Produto('barras de sabao', 5),
    Produto('copinhos de iogurte', 6)
]

# comeco da frase
resposta = 'Há '
for produto in produtos:
    # perguntar para cada produto
    produto.pergunta()
    # agregar a resposta de cada um na resposta final
    resposta += produto.resposta()

# colocar o 'e' entre sabao e iogurte
resposta = resposta.replace('o,', 'o e')
# colocar ponto no lugar da vírgula no final
resposta = resposta.replace('rte, ', 'rte.')

# mostrar a frase final
print(resposta)