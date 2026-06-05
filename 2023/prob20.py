num = int(input())
origNum = num

binValue = 512
usedNums = []
fBinNum = ""


while binValue != 0:
    binResult = 0
    if (num >= binValue):
        num -= binValue
        usedNums.append(binValue)
        binResult = 1

    fBinNum += str(binResult)

    print(f'{binValue}={binResult}')

    binValue = int(binValue / 2)

if (len(usedNums) > 1):
    for i in range(len(usedNums)):
        if (i == 0):
            sum = usedNums[0] + usedNums[1]
            print(f'{usedNums[0]}+{usedNums[1]} = {sum}')
        elif (i != 1):
            newSum = sum + usedNums[i]
            print(f'{sum}+{usedNums[i]} = {newSum}')
            sum = newSum
            

print(f'{origNum} = {fBinNum.lstrip("0")}')
