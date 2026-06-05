import math

baseNum = int(input())
largerNum = int(input())

x = int(math.log(largerNum, baseNum))
print(f'{baseNum}^{x} = {largerNum}')