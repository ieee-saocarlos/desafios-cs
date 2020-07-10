def deci2bin(num):

    if num > 1: 
        deci2bin(num // 2) 
    print(num % 2, end = '') 

def main():

    decimal = int(input('Digite um numero: '))

    deci2bin (decimal)



main()