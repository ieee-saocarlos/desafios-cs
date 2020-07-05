import time
print("oizinho\n")

Leite = int(input("leIte? "))
Ovo = int(input("OvO? "))
Prendedor = int(input("pendedor? "))
Barras_de_Sabão = int(input("barra de sabão? "))
Copinho_de_Iogurte = int(input("iogurtes? "))
print("")
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
print("")
print("fazendo contas   0%  [          ]")
time.sleep(0.4)
print("fazendo contas   10% [█         ]")
time.sleep(0.5)
print("fazendo contas   20% [██        ]")
time.sleep(0.6)
print("fazendo contas   30% [███       ]")
time.sleep(0.7)
print("fazendo contas   40% [████      ]")
time.sleep(0.8)
print("fazendo contas   30% [███       ]")
time.sleep(0.7)
print("fazendo contas   40% [████      ]")
time.sleep(0.8)
print("fazendo contas   50% [█████     ]")
time.sleep(0.9)
print("fazendo contas   50% [█████     ]")
time.sleep(0.9)
print("fazendo contas   60% [██████    ]")
time.sleep(1.0)
print("fazendo contas   70% [███████   ]")
time.sleep(1.1)
print("fazendo contas   80% [████████  ]")
time.sleep(1.2)
print("fazendo contas   90% [█████████ ]")
time.sleep(1.3)
print("fazendo contas   95% [██████████ ]")
time.sleep(1.4)
print("fazendo contas   99% [███████████ ]")
time.sleep(1.5)
print("fazendo contas   90% [█████████ ]")
time.sleep(2.5)
print("fazendo contas  100% [██████████]\n")
time.sleep(1.2)
print("perdi a conta, vc pode digitar tudo denovo?\n")
Leite2 = int(input("leIte? "))
Ovo2 = int(input("OvO? "))
Prendedor2 = int(input("pendedor? "))
Barras_de_Sabão2 = int(input("barra de sabão? "))
Copinho_de_Iogurte2 = int(input("iogurtes? "))
print("")
print("Há \
{0} caixas de leite, \
{1} ovos, \
{2} prendedores, \
{3} barras de sabão e \
{4} copinhos de iogurte."
                      .format(Leite*i, Ovo*j, Prendedor*k, Barras_de_Sabão*l, Copinho_de_Iogurte*m))
print("")
Sair = input("Escreva sair para sair\n")
if Sair == "sair":
    print("")
    print("Fechando o programa, não desligue o seu computador   0%  [          ]")
    time.sleep(0.4)
    print("Fechando o programa, não desligue o seu computador   10% [█         ]")
    time.sleep(0.5)
    print("Fechando o programa, não desligue o seu computador   20% [██        ]")
    time.sleep(0.6)
    print("Fechando o programa, não desligue o seu computador   30% [███       ]")
    time.sleep(0.7)
    print("Fechando o programa, não desligue o seu computador   40% [████      ]")
    time.sleep(0.8)
    print("Fechando o programa, não desligue o seu computador   50% [█████     ]")
    time.sleep(0.9)
    print("Fechando o programa, não desligue o seu computador   50% [█████     ]")
    time.sleep(0.9)
    print("Fechando o programa, não desligue o seu computador   60% [██████    ]")
    time.sleep(1.0)
    print("Fechando o programa, não desligue o seu computador   70% [███████   ]")
    time.sleep(1.1)
    print("Fechando o programa, não desligue o seu computador   80% [████████  ]")
    time.sleep(1.2)
    print("Fechando o programa, não desligue o seu computador   90% [█████████ ]")
    time.sleep(1.3)
    print("Fechando o programa, não desligue o seu computador  100% [██████████]\n")
    time.sleep(1.4)
    restart = True
    while restart:
        print("Fechar o programa não está respondendo\n")
        Sair2 = input("Aperte ENTER para fechar o programa\n")
        if Sair2 == "":
                continue
        else:
                break
else:
        print("")
        



