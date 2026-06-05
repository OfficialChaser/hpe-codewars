canRead = True

while canRead:
    mins = int(input())
    ending = "s"
    if (mins != -1):
        if (mins == 1):
            ending = ""
        print(f"You, {mins} minute{ending} ago.")
    else:
        canRead = False