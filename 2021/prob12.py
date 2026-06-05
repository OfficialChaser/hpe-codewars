# Calculations
def milesToYards(x):
    return (x * 1760)

def yardsToFeet(x):
    return (x * 3)

def inchesToFeet(x):
    return (x / 12)

def feetToMeters(x):
    return (x / 3.28)

def kmToMeters(x):
    return (x * 1000)

def cmToMeters(x):
    return (x / 100)

name, m, dUnits, _, tUnits = input().split(" ")
m = float(m)

# Distance Units
if (dUnits == "MILES"):
    m = milesToYards(m)
    m = yardsToFeet(m)
    m = feetToMeters(m)

elif (dUnits == "YARDS"):
    m = yardsToFeet(m)
    m = feetToMeters(m)

elif (dUnits == "FEET"):
    m = feetToMeters(m)

elif (dUnits == "INCHES"):
    m = inchesToFeet(m)
    m = feetToMeters(m)

elif (dUnits == "KILOMETERS"):
    m = kmToMeters(m)

elif (dUnits == "CENTIMETERS"):
    m = cmToMeters(m)

# Time units
if (tUnits == "HOUR"):
    # 3600 secs in an hour
    m /= 3600

elif (tUnits == "MINUTE"):
    # 60 secs in a minute
    m /= 60

h = (m ** 2) / (2 * 9.805)
sH = '{:.2f}'.format(h)
print(f"{name} will launch the messenger {sH} meters high", end=", ")

if (h > 50):
    print("OUCH!")
elif (h >= 25):
    print("SUCCESS!")
else:
    print("SPLAT!")