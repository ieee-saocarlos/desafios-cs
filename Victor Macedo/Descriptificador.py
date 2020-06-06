Chave=(input("Digite a Chave"))
NChave=len(Chave)
#Byte negativo
n=0
Lista_Chave=[]
for n in range (NChave):        #Transformo a string em lista
    Lista_Chave.append(Chave[n])
n=0
for n in range ((NChave-1),-1,-1):  #Inverto os bits e transformo em int
    if Lista_Chave[n]=='0':
        Lista_Chave.pop(n)
        Lista_Chave.insert(n,1)
    elif Lista_Chave[n]=='1':
        Lista_Chave.pop(n)
        Lista_Chave.insert(n,0)
n=0
for n in range ((NChave-1),-1,-1):  #Adiciono 1
    if Lista_Chave[n]==0:
        Lista_Chave.pop(n)
        Lista_Chave.insert(n,1)
        break
    elif Lista_Chave[n]==1:
        Lista_Chave.pop(n)
        Lista_Chave.insert(n,0)
#transformo byte em decimal
Chave_decimal=0
for n in range(NChave):
    Chave_decimal=Chave_decimal+(2**(7-n))*Lista_Chave[n]
###############################################################
Mensagem=int(input("Digite o código"))
Código=Mensagem//Chave_decimal
Código_st=str(Código);
n=0
NCódigo_st=len(Código_st)
Lista_Cód=[]
for n in range (0,NCódigo_st,+2):
    Lista_Cód.append(Código_st[n]+Código_st[n+1])
Lista_Cód.append("FIM")
k=0
n=0
#Tradução ASCII
for k in range (len(Lista_Cód)):
    if Lista_Cód[k]=="65":
        Lista_Cód.insert(k,"A")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="66":
        Lista_Cód.insert(k,"B")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="67":
        Lista_Cód.insert(k,"C")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="68":
        Lista_Cód.insert(k,"D")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="69":
        Lista_Cód.insert(k,"E")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="70":
        Lista_Cód.insert(k,"F")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="71":
        Lista_Cód.insert(k,"G")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="72":
        Lista_Cód.insert(k,"H")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="73":
        Lista_Cód.insert(k,"I")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="74":
        Lista_Cód.insert(k,"J")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="75":
        Lista_Cód.insert(k,"K")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="76":
        Lista_Cód.insert(k,"L")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="77":
        Lista_Cód.insert(k,"M")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="78":
        Lista_Cód.insert(k,"N")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="79":
        Lista_Cód.insert(k,"O")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="80":
        Lista_Cód.insert(k,"P")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="81":
        Lista_Cód.insert(k,"Q")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="82":
        Lista_Cód.insert(k,"R")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="83":
        Lista_Cód.insert(k,"S")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="84":
        Lista_Cód.insert(k,"T")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="85":
        Lista_Cód.insert(k,"U")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="86":
        Lista_Cód.insert(k,"V")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="87":
        Lista_Cód.insert(k,"W")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="88":
        Lista_Cód.insert(k,"X")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="89":
        Lista_Cód.insert(k,"Y")
        Lista_Cód.pop(k-1)
    if Lista_Cód[k]=="90":
        Lista_Cód.insert(k,"Z")
        Lista_Cód.pop(k-1)
Lista_Cód.pop(len(Lista_Cód)-1)
print(Lista_Cód)








