flag = 1
while flag == 1 :
    codigo = input("\rInsira aqui o codigo que voce recebeu: ").split('.')
    binary = list(codigo[1])
    chave = int(codigo[0])
    valor = 0
    mensagem =[]

    #Conversao de binario para decimal por complemento de 1
    for i in range(0,len(binary)-1):
        digito = binary[len(binary)-1-i]
        if digito == '0':
            valor = valor + pow(2, i)
    valor = valor + 1

    #Atribuicao do sinal do decimal se fosse necessário
    # if binary[0]=='1':
    #    valor = -valor

    #Separacao da mensagem em 2 digitos
    codcrip = str(chave//valor)
    ASCII = [(codcrip[i:i+2]) for i in range(0,len(codcrip),2)]

    #Traducao pelo codigo ascii
    for i in range(len(ASCII)):
        mensagem.append(chr(int(ASCII[i])))
    print(mensagem)

    if input("Digite END para encerrar o programa: ") == "END" or "End" or "end":
        flag = 0
    else:
        flag = 1






