startTime, endTime = input().split(" ")

sH, sM, sS = [int(i) for i in startTime.split(":")]
eH, eM, eS = [int(i) for i in endTime.split(":")]

sH *= 60
eH *= 60

cmMoved = 60 * ((eH + eM) - (sH + sM))
cmMoved += (eS - sS) + 40

cmRemaining = (500 - cmMoved)
metersRemaining = cmRemaining / 100
if (metersRemaining > 0):
    print('{:.2f}'.format(metersRemaining))
else:
    print("0.00")

while (cmRemaining % 20 != 0 and cmRemaining > 0):
    cmRemaining -= 1

width = int(cmRemaining / 20)
for _ in range(5):
    print("|" + width * " " + "|")

print("|" + width * "." + "|")

if (cmRemaining < 20):
    print("CURSE MY METAL BODY, I WASN'T FAST ENOUGH!")
elif (cmRemaining == 20):
    print("THIS IS SOME RESCUE!")
else:
    print("THE FORCE WAS WITH YOU")
