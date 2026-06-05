totalMonths = 0

bY, bM, bD = [int(i) for i in input().split("-")]
cY, cM, cD = [int(i) for i in input().split("-")]
name = input()

totalMonths += (cY - bY)
if (cM < bM):
    totalMonths -= 1
totalMonths *= 12

if (cM < bM):
    totalMonths += (cM + 12 - bM)
else:
    totalMonths += (cM - bM)

if (cD < bD):
    totalMonths -= 1

print(f'{name} is {totalMonths} months old')