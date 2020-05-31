# input()

Para receber uma entrada do usuário, é possível utilizar o comando *input()*. Ele é escrito da seguinte maneira:

nome = input("Por favor digite o seu nome: ")  
print("O nome digitado foi", nome )

Note que o valor recebido pelo *input()* é do tipo **str**, portanto, se o valor que deseja receber for um número inteiro, por exemplo, ele deverá ser transformado em int:

num = int(input("Por favor digite um número: "))  
print("O número digitado foi", num)
