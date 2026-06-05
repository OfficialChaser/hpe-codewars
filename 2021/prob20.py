numOfPancakes = int(input())

pckData = {}

for _ in range(numOfPancakes):
    height, label = input().split(" ")
    height = int(height)
    pckData[label] = height

values = list(pckData.values())
values.sort()

maxHeight = values[-1] + 1

keys = list(pckData.keys())
keys.sort()

sortedPckData = {}
for value in values:
    for key in keys:
        if pckData[key] == value:
            sortedPckData[key] = value

currHeight = maxHeight
for _ in range(maxHeight):
    for key in sortedPckData:
        if (sortedPckData[key] + 1 == currHeight):
            print("~", end="")
        elif (sortedPckData[key] + 1 > currHeight):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    currHeight -= 1

for letter in sortedPckData:
    print(letter, end="")
print()

