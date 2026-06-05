f = str(input().strip("F "))
k = str(input().strip("K "))
x = str(input().strip("X "))

missingVal = ""
result = 0

if (f == "?"):
    missingVal = "F"
    k = float(k)
    x = float(x)
    result = round((-k * x), 2)
elif (k == "?"):
    missingVal = "K"
    f = float(f)
    x = float(x)
    if (x != 0):
        result = round((-f / x), 2)
    else:
        print("K 0")
else:
    missingVal = "X"
    f = float(f)
    k = float(k)
    if (k != 0):
        result = round((-f / k), 2)
    else:
        print("X 0")

result = "{:.2f}".format(result)
print(f"{missingVal} {result}")