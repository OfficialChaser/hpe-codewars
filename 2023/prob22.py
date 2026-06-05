with open("input.txt", "r") as f:
    input = [i for i in f.read().strip().split('\n')]

labelTranslations = {
    "NICSRC": "source NIC",
    "NICDST": "destination NIC",
    "HDDSRC": "source drive",
    "HDDDST": "destination drive"
}

speeds = {}

for line in input:
    label, data = line.split(" ")
    mbs = 0
    if (label in labelTranslations):
        label = labelTranslations[label]
    else:
        label = label.lower()
    
    if ("NIC" in label or label == "router" or label == "switch" and data != "0"):
        data = float(data)
        mbs = ((data) * (10 ** 3)) / 8
    elif ("drive" in label):
        read, write = [float(i) for i in data.split("/")]
        if (label == "source drive"):
            mbs = read
        else:
            mbs = write
    else:
        continue

    speeds[mbs] = label

keys = list(speeds.keys())
keys.sort()
sortedSpeeds = {i: speeds[i] for i in keys}

for i, speed in enumerate(sortedSpeeds):
    if (i == 0):
        print('{:.1f}'.format(speed))
        print(sortedSpeeds[speed])
        break
    
