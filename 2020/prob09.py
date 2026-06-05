import math
canRead = True

while canRead:
    tMins, tSecs = [int(i) for i in input().split(" ")]
    if (tSecs >= 60):
        tMins += math.trunc(tSecs / 60)
        tSecs -= math.trunc(tSecs / 60) * 60
    if (tMins == 0 and tSecs == 0):
        canRead = False
    else:
        msg = ""
        secRemaining = 0
        minRemaining = 50 - tMins
        if (minRemaining <= 0):
            secRemaining = -tSecs
        if (tSecs > 0 and secRemaining >= 0):
            minRemaining -= 1
            secRemaining = 60 - tSecs
        if (minRemaining < 0):
            msg = "(we're gonna need a bigger record)"
        elif (minRemaining < 25):
            msg = "(we'll need both sides)"
        print(f"Time remaining {minRemaining} minutes and {secRemaining} seconds {msg}")