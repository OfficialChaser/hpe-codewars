word = input()
size = int(input())


lettersToPrint = []
c = 0
for i in range((size - 2) * 4 + 4):
    if (c == len(word)):
        c = 0
    lettersToPrint.append(word[c])
    c += 1

tRow = lettersToPrint[:size]

for char in tRow:
    print(char, end="")
print()

if (size > 2):
    lRow = lettersToPrint[(size - 2) * 4 - 1: len(lettersToPrint)]
    lRow = lRow[::-1]
    rRow = lettersToPrint[size: (size - 2) * 2 + 2]
    
    for i, char in enumerate(lRow):
        row = []
        row.append(char)
        [row.append(" ") for i in range(size - 2)]
        print(len(rRow))
        try:
            row.append(rRow[i])
        except IndexError:
            break
        for char in row:
            print(char, end="")
        print()

bRow = lettersToPrint[(size - 2) * 2 + 2: (size - 2) * 3 + 4]
bRow = bRow[::-1]


for char in bRow:
    print(char, end="")
print()