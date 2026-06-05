import math

wallHeight, punchHeight, anger = input().split(" ")

wallHeight = int(wallHeight)
punchHeight = int(punchHeight)
anger = int(anger)

if (punchHeight > wallHeight or punchHeight == 0):
    for _ in range(wallHeight):
        print("#")
else:
    fallenBricks = wallHeight - (punchHeight - 1)
    wallHeight -= fallenBricks

    x = wallHeight
    for brick in range(wallHeight):
        if (x > 1):
            print("#")
        else:
            print("#", end="")
            break
        x-= 1

    if (anger >= 10):
        periods =  int(math.trunc(anger / 10))
        for i in range(periods):
            print(".", end="")

    for brick in range(fallenBricks):
        print("#", end="")

    print()