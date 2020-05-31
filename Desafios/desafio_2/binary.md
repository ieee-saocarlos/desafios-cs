# Números binários

Os números binários são uma outra forma de representar os números. Esse sistema é utilizado pelos computadores para processar e armazenar os dados, por isso é muito importante que um programador saiba como eles funcionam e algumas de suas propriedades.

## Representando números binários

Provavelmente você conhece bem os números na base decimal, cada dígito representa uma potência de dez. Dessa forma, o número 1234 possui o valor representado por $1 \cdot 10^{3} + 2 \cdot 10^{2} + 3 \cdot 10^{1} + 4 \cdot 10^{0} $. Da mesma forma, o binário 1001 equivale a $1 \cdot 2^{3} + 0 \cdot 2^{2} + 0 \cdot 2^{1} + 1 \cdot 2^{0} = 9$.

## Convertendo números decimais em binários

O algoritmo mais utilizado para transformar decimais em binários utiliza a divisão consecutiva do número decimal por dois. Veja esta [imagem](https://image.slidesharecdn.com/lecture2ns-140606050500-phpapp02/95/lecture-2-ns-9-638.jpg?cb=1402031166) para visualizar o algoritmo.

De forma resumida, basta ir dividindo o número decimal por dois e armazenando os restos das divisões em uma pilha. Essa pilha pode ser uma string. Dessa forma, é possível facilmente fazer essa conversão armazenando os restos em uma variável utilizando operações de strings. 

Quando o resultado da divisão finalmente der 0, basta pegar os restos, sendo o primeiro resto o [bit menos significativo](https://pt.wikipedia.org/wiki/Bit_mais_significativo) do binário.

## Convertendo binários em decimais

Como foi dito no início desse documento, cada bit (algarismo) do número binário representa o seu valor multiplicado por uma potência de 2. Portanto basta realizar essa conta para transformar o binário em decimal.

