canRead = True
while canRead:
    h, l, fChoice = input().split(" ")
    h = int(h)
    l = int(l)
    if (h == 0 and l == 0 and fChoice == "S"):
        canRead = False
    else:
        if (fChoice == "S"):
            h += 40
            totLen = (2 * h) + (2 * l)
            print(f"Square {totLen}")
        else:
            h += 80
            l += 80
            totLen = (2 * h) + (2 * l)
            print(f"Diagonal {totLen}")