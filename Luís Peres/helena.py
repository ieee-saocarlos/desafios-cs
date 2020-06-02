def verifyByte(byte):
    # verify if the string contains 8 digits that are 1 or 0
    if (len(byte) != 8) or (byte.count('1') + byte.count('0') != 8):
        print("Essa entrada nao e' um byte valido (8 bits)!")
        return False
    else: return True


def binaryToDecimal(binary):
    """
    8 bits (1 byte), being the MSD the sign
    binary:  string input
    decimal: string output
    """
    # verify if the input has 8 bits
    if not verifyByte(binary): return "Tente novamente."

    decimal = 0                 # declare storage variable
    N = len(binary) - 1         # size in bits
    for bit in range(N, -1, -1):# for each bit
        # multiply the bit (0/1) by its value (2 ** i)
        decimal += int(binary[bit]) << (N - bit)

    sign = int(binary[0])       # verify for negative sign
    if sign == 1: decimal = -((decimal ^ 0xff) + 1)
        # complementary of two: invert every bit and then add 1
        # (1111 1111 XOR 0101 1100) + 1 = (1010 0011) + 1 = 1010 0100
        # (0xff ^ 0x5c) + 0x01 = 0xa4
        # A XOR 1 = /A        
    
    return '{}'.format(decimal) # must return string


def decimalToBinary(decimal):
    """
    decimal: string input
    binary:  string output
    """
    decimal = int(decimal)      # convert to number
    if decimal < 0:             # verify for negative sign
        decimal = ((abs(decimal) - 1) ^ 0xff)
        # invert before converting to binary!
        # complement of two: subtract 1 then invert every bit
        # 1111 1111 XOR (0101 1100 - 1) = 1111 1111 XOR (0101 1011) = 1010 0100
        # 0xff ^ (0x5c - 0x01) = 0xa4
        # A XOR 1 = /A
    
    binary = ''                 # declare storage variable
    while decimal > 0:          # divide by 2 and store remainder
        binary = '{}'.format(decimal % 2) + binary
        decimal //= 2           # floor division

    return '{}'.format(binary)  # must return string

def decrypt(crypto):
    # split the string using the dot as a divider
    cryptoMsg, cryptoKey = crypto.split(".")

    # convert the key: pass the string as input
    key = binaryToDecimal(cryptoKey)

    # using the key to decrypt the message: floor division
    message = '{}'.format(int(cryptoMsg) // abs(int(key)))

    messageASCII = ''           # declare storage variable
    for char in range(0, len(message), 2):
        # for every 2 numbers, concatenate the corresponding char to the string
        messageASCII += chr(int(message[char:char+2]))

    return {                    # a dictionary with all data before and after decrypting
        "encrypted key": cryptoKey, "encrypted message": cryptoMsg,
        "key": key, "message": message, "messageASCII": messageASCII
        }

messages = {                    # the three provided messages
    'taskMsg': '586224859023584394875746663987064310875575294287428749066042620660.10101100',
    'linkMsg': '867435468107816593411652410117813.11110101',
    'helenaMsg': '3168969701683105067532556300039069.11010101'
}

for msg in messages:            # show the decrypted messages
    print(decrypt(messages[msg])['messageASCII'])