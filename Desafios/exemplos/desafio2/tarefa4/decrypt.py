crypt = input("enter the cryptographed message: ")
message = int(crypt[0:34])
key = int(crypt[-8:])

print((message, key))

real_key = bin(int(str(11111111 - key), 2) + int("0b1", 2))[2:]

b_num = list(real_key)
value = 0

for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)

num_message = str(int(message) // int(value))

for i in range(len(num_message)//2):
    print(chr(int(num_message[(2*i):(2*i+2)])), end='')
