import math

s = input()
result = ""
for char in s:
    dec = ord(char)
    base6num = ""
    digit1 = str(math.trunc(dec / 36))
    base6num += digit1
    dec -= int(digit1) * 36
    digit2 = str(math.trunc(dec / 6))
    base6num += digit2
    dec -= int(digit2) * 6
    base6num += str(dec)
    result += base6num

print(result)