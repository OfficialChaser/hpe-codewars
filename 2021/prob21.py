width = 0
with open("input.txt", "r") as file:
    data = [i for i in file.read().strip().split("\n")]
    width = len(data[0])

found = False

for y, line in enumerate(data):
    listLine = list(line)
    if (found):
        break

    # Horizontal first
    for x, char in enumerate(listLine):
        if (char == "M" and x < width - 3):
            if (listLine[x + 1] == "O" and listLine[x + 2] == "J" and listLine[x + 3] == "O"):
                for j in range(4):
                    print(f'{listLine[x + j]}: {x + j},{y}')
                found = True
                break
        # Backwards
        elif (char == "O" and x < width - 3):
            if (listLine[x + 1] == "J" and listLine[x + 2] == "O" and listLine[x + 3] == "M"):
                startingX = x + 3
                for j in range(4):
                    print(f'{listLine[startingX - j]}: {startingX - j},{y}')
                found = True
                break
        
        # Top to bottom
        if (char == "M" and y < width - 3):
            if (data[y + 1][x] == "O" and data[y + 2][x] == "J" and data[y + 3][x] == "O"):
                for j in range(4):
                    print(f'{data[y + j][x]}: {x},{y + j}')
                found = True
                break
        # Bottom to top
        elif (char == "O" and y < width - 3):
            if (data[y + 1][x] == "J" and data[y + 2][x] == "O" and data[y + 3][x] == "M"):
                startingY = y + 3
                for j in range(4):
                    print(f'{data[startingY - j][x]}: {x},{startingY - j}')
                found = True
                break
        
        # Square
        if (char == "M" and x < width - 1):
            if (listLine[x + 1] == "O"):
                if (y < width - 1):
                    if (data[y + 1][x] == "J" and data[y + 1][x + 1] == "O"):
                        for j in range(2):
                            print(f'{listLine[x + j]}: {x + j},{y}')
                        for j in range(2):
                            print(f'{data[y + 1][x + j]}: {x + j},{y + 1}')
                        found = True
                        break
