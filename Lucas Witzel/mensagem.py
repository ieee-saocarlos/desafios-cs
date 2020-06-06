print("Digite o número da mensagem secreta: ")
segredo = int(input())

print("Digite o binário negativo: ")
binario_negativo = int(input())
v = []
b = str(binario_negativo)
for bits in b:
    v.append(int(bits))

i = len(v)
for j in range(0, i):
    if v[j] == 0:
        v[j] = 1
    else:
        v[j] = 0

n = i - 1
v[n] += 1
while n >= 0:
    if v[n] == 2:
        v[n] = 0
        v[n - 1] += 1
        n -= 1
    else:
        break
'''   
if v[0]==2:
    i+=1
    for j in range(i-1,1,-1):
        v[j]=v[j-1]
    v[0]=1
    v[1]=0
'''

chave = 0
e = i - 1
for j in range(0, i):
    chave += v[j] * (2**e)
    e -= 1

mensagem = segredo // chave

m = mensagem
k = 0
while m != 0:
    m = m // 10
    k += 1

k -= 2
simbolos = []
while mensagem != 0:
    simbolos.append(mensagem // (10**k))
    mensagem = mensagem % (10**k)
    k -= 2

s = len(simbolos)
letras = chr
for j in range(0, s):
    letras = chr(simbolos[j])
    print(letras, end="")

input()