import random
word = input("Insira a frase a ser criptografada: ")
to_decimal = ''

# transforma a palavra em numeros pela tabela ASCII
for i in word:
    to_decimal += str(ord(i))

# gera uma chave aleatória
key = random.randint(10, 2 ** 7 - 1)

# criptografa a mensagem utilizando a chave
message = int(to_decimal) * key

# faz o complemento de dois da chave gerada para criar a que ficará a mostra
public_key = int(bin(key)[2:])
public_key = bin(int(str(11111111 - public_key), 2) + int("0b1", 2))[2:]

# gera uma mensagem criptografada com uma chave separados por um ponto
public_message = str(message) + '.' + str(public_key)

print(public_message)
