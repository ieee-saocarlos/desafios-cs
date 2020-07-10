#!/usr/bin/python3

def bin_add_one(lbin):
    for d in range(len(lbin)-1, 0, -1):
        if lbin[d] == 1:
            lbin[d] = 0
        else:
            lbin[d] = 1
            break
    return lbin


def bin2udec(sbin):
    sbin = list(sbin)
    n = 0
    for d in range(len(sbin)-1, 0, -1):
        n = n + (2**(7-d))*int(sbin[d])
    return n


def bin2dec(sbin):
    if sbin[0] == '0':
        return bin2udec(sbin)
    # inverte bits e converte para lista de ints em uma lambda
    ibin = list(map(lambda b: 0 if b == '1' else 1, list(sbin)))
    ibin = bin_add_one(ibin)
    ssbin = list(map(lambda i: str(i), ibin))
    d = bin2udec(ssbin)
    return -d


msg = input("Menssagem Codificada: ")
key = msg.split('.')[1]
msg = int(msg.split('.')[0])
msg = str(msg // abs(bin2dec(key)))
s = []
for i in range(0, len(msg), 2):
    s.append(chr(int(msg[i]+msg[i+1])))
print("Mensagem Decodificada:\t", "".join(s))
