end = False

while not end:
    num = input()

    if num == "000":
        end = True
        continue
    
    res = 0
    mult = 1

    for d in num[::-1]:
        res += int(d) * mult
        mult *= 4
    
    print(res)