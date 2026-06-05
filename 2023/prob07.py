canRead = True

while canRead:
    num = int(input())
    if (num != 0):
        if (num % 5 == 0 and num % 9 == 0):
            print(num, "FIZZ FUZZ!")
        elif (num % 5 == 0):
            print(num, "FIZZ")
        elif (num % 9 == 0):
            print(num, "FUZZ")
    else:
        canRead = False