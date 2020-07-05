# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:00:23 2020

@author: allan
"""
complementar = {"0" : "1", "1" : "0"} #convertedor
binario = ""
texto = ""
codigo = input("Codigo Secreto\n")
separado = codigo.split(".") #[0]ASCII [1]binario negativo
a = 0
for a in separado[1]: # 0 vira 1 e 1 vira 0
    negativo = complementar[a]
    binario = binario + negativo
chave = int(binario, 2) + 1 #binario positivo
print(chave)
divide = str(int(separado[0])//(chave)) #dividindo
print (divide, len(divide)) #testes
for a in range(0, len(divide),2):
    b = chr(int(divide[a]+divide[a+1]))
    texto = texto + b
print(texto)