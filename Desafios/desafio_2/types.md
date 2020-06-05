# Tipos de variáveis

Os bytes na memória do seu computador podem ser interpretados de diversas formas. Por exemplo, se eu escrever 1000001‬ ele pode ser um número binário, mas também pode ser o decimal 65, ou então a letra "A" na tabela [ASCII](https://pt.wikipedia.org/wiki/ASCII), pode ainda ser uma string formada por caracteres 1 e 0. Isso vai depender do tipo de valor e das operações que forem aplicadas nesse valor. 

Em Python, cada valor é chamado de objeto, e cada objeto possui um tipo. Há diversos tipos como: Inteiro (int), números decimais (float), booleano (bool), string (str), list, tuple, set, dictionary (dict) e None.

Neste momento iremos focar nos tipos int, float e str.

## int

Números inteiros em Python possuem o tipo *int*.


# Tipos de variáveis

Os bytes na memória do seu computador podem ser interpretados de diversas formas. Por exemplo, se eu escrever 1000001‬ ele pode ser um número binário, mas também pode ser o decimal 65, ou então a letra "A" na tabela [ASCII](https://pt.wikipedia.org/wiki/ASCII), pode ainda ser uma string formada por caracteres 1 e 0. Isso vai depender do tipo de valor e das operações que forem aplicadas nesse valor. 

Em Python, cada valor é chamado de objeto, e cada objeto possui um tipo. Há diversos tipos como: Inteiro (int), números decimais (float), booleano (bool), string (str), list, tuple, set, dictionary (dict) e None.

Neste momento iremos focar nos tipos int, float e str.

## int e float

Números inteiros em Python possuem o tipo *int* e 
números com valores fracionários (ponto flutuante) possuem o tipo *float* e com eles é possível realizar operações numéricas:

Operação                   | Operador
---------------------------|-------------
Adição 	                   | x + y
Subtração                  | x - y
Multiplicação              | x * y
Divisão                    | x / y
Divisão piso               | x // y
Resto da divisão ou módulo | x % y
Exponenciação              | x ** y
Converter para float       | float(x)
Converter para int         | int(x)
Valor absoluto             | abs(x)
Arredondamento             | round(x) 

## str

Strings são sequencias de caracteres e são representados entre aspas simples ('') ou duplas ("") indiferentemente. Caso queira definir uma string que possua aspas simples como a palavra don't, é possível fazer utilizando aspas duplas - "don't". Com elas também é possível realizar operações que são descritas logo após a tabela:

Operação                   | Operador
---------------------------|-------------
Indexação (índices) 	   | s[x]
Concatenação               | s + t
Tamanho (length)           | len(s)
Valores ordinários (ASCII) | ord(n)
Valor do caractere (ASCII) | chr(x)
Converter para string      | str(x)
Converter para int         | int(s)
Converter para float       | float(x)

Os exemplos a seguir tomam como "s" a string "Palavra", "t" a string "IEEE" e "n" o número 65

* **Indexação** é pegar o caractere dando o índice dele na string: s[3] -> 'a'. \
É possível também pegar intervalos: s[1:4] -> 'ala'
* **Concatenação** é a soma de strings: s + t -> 'PalavraIEEE'
* **Tamanho** dá o tamanho da string: len(s) -> 7
*  **Valores ordinários e do caractere** transformam um caractere em seu número correspondente na tabela ASCII e o númere no caractere correspondente respectivamente: ord('A') -> 65; chr(65) -> 'A'

Referências: [Python docs tipos numéricos](https://docs.python.org/3/library/stdtypes.html#typesnumeric) e "Python programming fundamentals" de Kent D. LEE