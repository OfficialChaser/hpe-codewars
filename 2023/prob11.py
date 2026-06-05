import math

students = int(input())

fCarsNeeded = math.trunc(students / 4)
pCar = students % 4
if (fCarsNeeded > 1):
    print(f"{fCarsNeeded} full cars", end=", " if pCar >= 1 else "\n")
elif (fCarsNeeded == 1):
    print(f"1 full car", end=", " if pCar >= 1 else "\n")

if (pCar >= 1):
    print("1 partial car")
