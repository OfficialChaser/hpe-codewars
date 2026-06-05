canRead = True

gemstones = {
    "Lapis":[],
    "Topaz":[],
    "Tourmaline":[],
    "Sapphire":[],
    "Peridot":[],
    "Ruby":[],
    "Pearl":[],
    "Emerald":[],
    "Diamond":[],
    "Aquamarine":[],
    "Amethyst":[],
    "Garnet":[]
}

regularNames = []
gemNames = []
while canRead:
    name = input()
    if (name != "END"):
        hasGemName = False
        nameParts = name.split(" ")
        for part in nameParts:
            if (part in gemstones):
                gemNames.append(name)
                hasGemName = True
                break
        if (not hasGemName):
            regularNames.append(name)
    else:
        canRead = False

if (len(gemNames) == 1):
    print(gemNames[0])


elif (len(gemNames) >= 2):
    namesPrinted = []
    for gem in gemstones:
        tmp = []
        for name in gemNames:
            if (gem in name and name not in namesPrinted):
                tmp.append(name)
                namesPrinted.append(name)
                break
        tmp.sort()
        if (len(tmp) > 0):
            [print(i) for i in tmp]

regularNames.sort()
[print(i) for i in regularNames]