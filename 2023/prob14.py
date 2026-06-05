tribSeq = [0, 1, 1]
for i in range(33):
    newNum = tribSeq[i] + tribSeq[i + 1] + tribSeq[i + 2]
    tribSeq.append(newNum)

canRead = True
while canRead:
    m, n = [int(i) for i in input().split(" ")]
    if (m == 0 and n == 0):
        canRead = False
    else:
        print(tribSeq[m] - tribSeq[n])