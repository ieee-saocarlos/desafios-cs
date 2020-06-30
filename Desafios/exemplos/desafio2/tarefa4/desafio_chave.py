secret = 10111100

r = str(11111111 - secret)

b = r.zfill(8)

print(b)

decimal = (int(b[0]) * 128 + int(b[1])* 64 + int(b[2])* 32 + int(b[3])* 16 +
           int(b[4])* 8 + int(b[5])* 4 + int(b[6])* 2 + int(b[7])* 1 + 1)

print(decimal)

n = 50113939468477010370282269327756775620 // decimal

s = str(n)

print(s)


print(len(s))


print( chr(int(s[0:2])), chr(int(s[2:4])), chr(int(s[4:6])), chr(int(s[6:8])),
       chr(int(s[8:10])), chr(int(s[10:12])), chr(int(s[12:14])), chr(int(s[14:16])),
       chr(int(s[16:18])), chr(int(s[18:20])), chr(int(s[20:22])), chr(int(s[22:24])),
       chr(int(s[24:26])), chr(int(s[22:24])), chr(int(s[24:26])), chr(int(s[26:28])),
       chr(int(s[28:30])), chr(int(s[30:32])), chr(int(s[32:34])),chr(int(s[34:36])))


