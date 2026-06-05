treble, mPitch = input().split(" ")
treble = float(treble)
mPitch = float(mPitch)

bassDrop = round(((mPitch / 3.43) * treble), 1)
print(bassDrop, end=" ")

if (bassDrop >= 75.0 and bassDrop <= 85.0):
    print("NOW")
else:
    print("WAIT FOR IIIIIT")