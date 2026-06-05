sticks, sSize, tenLim = input().split(" ")
sticks = float(sticks)
tenLim = float(tenLim)
if ("/" in sSize):
    num, denom = [float(i) for i in sSize.split("/")]
    size = num / denom
else:
    size = float(sSize)

sticks *= size
weight = sticks * 0.45
expForce = round((weight * 7.5), 2)
print('{:.2f}'.format(expForce), end=" ")

if (expForce <= tenLim):
    print("the Mask can eat it!")
else:
    print("the Mask should not eat it!")
