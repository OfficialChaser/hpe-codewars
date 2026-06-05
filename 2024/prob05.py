decValues = [int(i) for i in input().split(" ")]

finalStr = ""

for value in decValues:
    char = chr(value)
    finalStr += char

print(finalStr)