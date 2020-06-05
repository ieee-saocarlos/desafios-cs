# Números binários

Os números binários são uma outra forma de representar os números. Esse sistema é utilizado pelos computadores para processar e armazenar os dados, por isso é muito importante que um programador saiba como eles funcionam e algumas de suas propriedades.

## Representando números binários

Provavelmente você conhece bem os números na base decimal, cada dígito representa uma potência de dez. Dessa forma, o número 1234 possui o valor representado por 1 x 10^3 + 2 x 10^2 + 3 x 10^1 + 4 x 10^0. Da mesma forma, o binário 1001 equivale a 1 x 2^3 + 0 x 2^2+ 0 x 2^1 + 1 x 2^0 = 9.

## Convertendo números decimais em binários

O algoritmo mais utilizado para transformar decimais em binários utiliza a divisão consecutiva do número decimal por dois. Veja esta [imagem](https://image.slidesharecdn.com/lecture2ns-140606050500-phpapp02/95/lecture-2-ns-9-638.jpg?cb=1402031166) para visualizar o algoritmo.

De forma resumida, basta ir dividindo o número decimal por dois e armazenando os restos das divisões em uma pilha. Essa pilha pode ser uma string. Dessa forma, é possível facilmente fazer essa conversão armazenando os restos em uma variável utilizando operações de strings. 

Quando o resultado da divisão finalmente der 0, basta pegar os restos, sendo o primeiro resto o [bit menos significativo](https://pt.wikipedia.org/wiki/Bit_mais_significativo) do binário.

## Convertendo binários em decimais

Como foi dito no início desse documento, cada bit (algarismo) do número binário representa o seu valor multiplicado por uma potência de 2. Portanto basta realizar essa conta para transformar o binário em decimal.

## Binários negativos

Como representar um binário negativo sendo que não queremos utilizar o simbolo '-'?  Isso pode ser feito de diversas formas. Uma delas é utilizar o bit mais a esquerda para representar o sinal. Dessa forma, 10 = 01010 e -10 = 11010. No entanto, por motivos técnicos uma outra forma de representação é mais comum, devido a facilitade de realizar operações aritméticas com números negativos.

Imagine como funcionam os negativos decimais. O oposto de um número é aquele que quando somado ao número resulta em zero. Portanto iremos utilizar esse mesmo princípio para definir os binários negativos.

Por exemplo, o positivo 12 ainda será representado por 01100, mas o -12 será escrito como 10100. Assim 01100 + 10100 resulta em 100000, que seria 0 se tomar os 5 primeiros números.

Para obter o binário negativo dessa forma, utiliza-se o complemento de dois. Basicamente isso equivale a inverter os 0's e 1's do número e somar 1 ao resultado. Dessa forma, tomando o exemplo anterior 01100 vira 10011, que quando somado a 1 vira 10100. Fazendo o complemento de dois novamente, volta-se ao número original.

Ao utilizar o complemento de 2, é importante saber o tamanho do número. Uma definição comum é a de byte. Que representa binários com 8 dígitos. Note também que os números negativos sempre iniciam com 1 e os positivos iniciam com 0, mesmo utilizando complemento de dois.

