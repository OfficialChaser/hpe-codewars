import math

name = input()
rampLen = int(input())
accRate = float(input())
rivWidth = float(input())

time = math.sqrt((2 * rampLen) / accRate)
speed = round((time * accRate), 2)
dist = round(((speed ** 2) / 9.805), 1)

result = ""

if (rivWidth - 5 > dist):
    result = "SPLASH"
elif (dist >= rivWidth - 5 and dist <= rivWidth):
    result = "BARELY MADE IT"
elif (dist > rivWidth):
    result = "LIKE A BOSS"

sSpeed = '{:.2f}'.format(speed)
sDist = '{:.1f}'.format(dist)
print(f"{name} will reach a speed of {sSpeed} m/s on a {rampLen} meter ramp, crossing {sDist} of {rivWidth} meters", end=", ")
print(f'{result}!')

