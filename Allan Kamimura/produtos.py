print("oizinho")
Leite = int(input("leIte?"))
Ovo = int(input("OvO?"))
Prendedor = int(input("pendedor?"))
Barras_de_Sabão = int(input("barra de sabão?"))
Copinho_de_Iogurte = int(input("iogurtes?"))
i = 1
while i < 12:
        print("leite:", Leite*i)
        i += 1
n=1
while n < 100:
        print("loading",n-1,"% fazendo contas.........")
        print("loading",n-2,"% fazendo contas.........")
        print("loading",n,"% fazendo contas.........")
        n += 1
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
print("perdi a conta, vc pode digitar tudo denovo?")
Leite2 = int(input("leIte?"))
Ovo2 = int(input("OvO?"))
Prendedor2 = int(input("pendedor?"))
Barras_de_Sabão2 = int(input("barra de sabão?"))
Copinho_de_Iogurte2 = int(input("iogurtes?"))
print("Há",Leite*i,"caixas de leite,", Ovo*j,"ovos,",Prendedor*k,"prendedores,",Barras_de_Sabão*l,"barras de sabão,",Copinho_de_Iogurte*m,"copinhos de iogurte")


