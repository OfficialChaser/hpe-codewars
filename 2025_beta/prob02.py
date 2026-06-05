end = False
failed = False

while not end:
    num = int(input())
    if num == 0:
        break
    if num % 2 == 1:
        failed = True
        print(f"{num} is odd")

if failed:
    print("FLASH FAILED")
else:
    print("FLASH FORWARD")
