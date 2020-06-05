# .format()

Uma forma mais elegante de escrever saídas para o usuário é utilizando a função .format(). Ela é utilizada juntamente com o print para incluir variáveis dentro de um texto.

## strings

Para mexer com strings, basta dizer onde ficará cada valor utilizando chaves '{}'. Caso queira dizer a ordem em que elas ficarão, utiliza-se os índices iniciando em 0. 

**print('{} e {}'.format('ovos', 'bacon'))**
#ovos e bacon

**print('{0} e {1}'.format('ovos', 'bacon'))**
#ovos e bacon

**print('{1} e {0}'.format('ovos', 'bacon'))**
#bacon e ovos

## int e float

para int, utiliza-se o identificador "d" e para float utiliza-se o "f". Basicamente digita-se o índice depois dois pontos e o tipo de valor, exemplos:

**print("Eu comi {0.d} grandes {1}".format(2, "Peras"))** #Eu comi 2 grandes Peras

**print ("Minha média nesse {0} foi {1:.0f}%".format("semestre", 7.23))** #Minha média nesse semestre foi 7.23

s – strings \
d – inteiros base 10 \
f – floating point display \
c – character \
b – binary \
o – octal \
x – hexadecimal with lowercase letters after 9 \
X – hexadecimal with uppercase letters after 9 \
e – notação exponencial (0.000000123 é escrito como 1.23E-7)

[input e output](https://docs.python.org/pt-br/3/tutorial/inputoutput.html) e [geeks](https://www.geeksforgeeks.org/python-format-function/)