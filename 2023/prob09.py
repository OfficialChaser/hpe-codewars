import math

numOfCars = int(input())
raceLen = int(input())
for i in range(numOfCars):
    mph, car = input().split(" ")
    mph = int(mph)

    totMiles = raceLen * (mph / 60)
    truncTotMiles = math.trunc(totMiles * 100) / 100
    truncTotMiles = '{:.2f}'.format(truncTotMiles)

    dashes = math.trunc(totMiles / 5)
    totMiles -= math.trunc(totMiles / 5) * 5

    tildes = math.trunc(totMiles)
    totMiles -= math.trunc(totMiles)
    
    curlyBraces = math.trunc(totMiles * 4)

    print(f'({truncTotMiles})', end ="")
    for _ in range(dashes):
        print("-", end="")
    for _ in range(tildes):
        print("~", end="")
    for _ in range(curlyBraces):
        print("{}", end="")
    print(car)
    
    