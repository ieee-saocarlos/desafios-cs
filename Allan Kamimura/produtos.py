import time
print("oizinho\n")


Leite = int(input("leIte?"))
Ovo = int(input("OvO?"))
Prendedor = int(input("pendedor?"))
Barras_de_Sabão = int(input("barra de sabão?"))
Copinho_de_Iogurte = int(input("iogurtes?"))


i = 1
while i < 12:
        print("leite:", Leite*i)
        i += 1
j=1
while j < 12:
        print("ovos:", Ovo*j)
        j += 1
k=1
while k < 24:
    print("prendedores:" , Prendedor*k)
    k += 1
l=1
while l < 5:
    print("barras de sabão:", Barras_de_Sabão*l)
    l  += 1
m=1
while m < 6:
    print("copinhos de iogurte:", Copinho_de_Iogurte*m)
    m += 1
    
    
print("fazendo contas [          ] loading 0%")
time.sleep(0.4)
print("fazendo contas [#         ] loading 10%")
time.sleep(0.5)
print("fazendo contas [##        ] loading 20%")
time.sleep(0.6)
print("fazendo contas [###       ] loading 30%")
time.sleep(0.7)
print("fazendo contas [####      ] loading 40%")
time.sleep(0.8)
print("fazendo contas [###       ] loading 30%")
time.sleep(0.7)
print("fazendo contas [####      ] loading 40%")
time.sleep(0.8)
print("fazendo contas [#####     ] loading 50%")
time.sleep(0.9)
print("fazendo contas [#####     ] loading 50%")
time.sleep(0.9)
print("fazendo contas [######    ] loading 60%")
time.sleep(1.0)
print("fazendo contas [#######   ] loading 70%")
time.sleep(1.1)
print("fazendo contas [########  ] loading 80%")
time.sleep(1.2)
print("fazendo contas [######### ] loading 90%")
time.sleep(1.3)
print("fazendo contas [########## ] loading 95%")
time.sleep(1.4)
print("fazendo contas [########### ] loading 99%")
time.sleep(1.5)
print("fazendo contas [######### ] loading 90%")
time.sleep(2.5)
print("fazendo contas [##########] loading 100%\n")
time.sleep(1.2)
print("perdi a conta, vc pode digitar tudo denovo?\n")
Leite2 = int(input("leIte?"))
Ovo2 = int(input("OvO?"))
Prendedor2 = int(input("pendedor?"))
Barras_de_Sabão2 = int(input("barra de sabão?"))
Copinho_de_Iogurte2 = int(input("iogurtes?"))


print("Há",Leite*i,"caixas de leite,", Ovo*j,"ovos,",Prendedor*k,"prendedores,",Barras_de_Sabão*l,"barras de sabão,",Copinho_de_Iogurte*m,"copinhos de iogurte")
input("Aperte Enter para sair")

