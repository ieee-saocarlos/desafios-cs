## Declaração e atribuição de variáveis

Para declarar uma variável basta escrever o nome que deseja dar avariável e depois escrever o valor desta variável, separando os dois por '=':
* palavra = 5
* numero_primo = 'oi'
* fruta = 2.1
* decimal = 'IEEE'

Para atribuir outro valor à variável, basta utilizar o nome dela na atribuição:
* palavra = 'IEEE'
* numero_primo = 3
* fruta = 'banana'
* decimal = 56.40

É possível agora printar todas essas variáveis juntas:

**print(palavra, fruta,  numero_primo, decimal)
IEEE 3 banana 56.40**

É possível concatenar as strings e printá-las juntas:

**print(palavra + fruta)
IEEEbanana**

Finalmente, vamos tentar fazer isso ter algum sentido:

**print('No dia', numero_primo, 'o', palavra, 'irá sortear uma', fruta, 'no valor de', decimal, 'reais')**

Que resultará em: 

**No dia 3 o IEEE irá sortear uma banana no valor de 56.4 reais**

Essa não é a melhor forma, mas é possível retornar valores para o usuário dessa forma.

