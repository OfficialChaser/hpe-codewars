lists = {1: [], 2: [], 3: [], 4: [], 5: []}

while True:
    num = int(input())
    if num == 0:
        break
    elif num in lists:
        lists[num].append(num)
    
currentNum = 5
sum = 0
totalNums = 0

altFormat = False

for _ in lists:
    if len(lists[currentNum]) >= 10:
        altFormat = True
        break
    currentNum -= 1

currentNum = 5
for _ in lists:

    numOfNums = len(lists[currentNum])
    if (altFormat == False):
        print(f"{currentNum} ({numOfNums}) |", end="")
    else: 
        if (numOfNums >= 10):
            print(f"{currentNum} ({numOfNums}) |", end="")
        else:
            print(f"{currentNum} ( {numOfNums}) |", end="")

    for i in range(numOfNums):
        print("=", end="")
    
    totalNums += numOfNums
    sum += (numOfNums * currentNum)

    print()
    currentNum -= 1


avg = sum / totalNums
avg_truncated = int(avg * 100) / 100
avg_truncated = "{:.2f}".format(avg_truncated)
print(f"Average efficiency: {avg_truncated}")