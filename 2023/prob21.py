with open("input.txt", "r") as file:
    data = [i for i in file.read().strip().split('\n')]

raceLen = float(data[0])

originalOrder = []
results = {}
for i in range(1, len(data) - 1):
    name, raceInfo = data[i].split(" ")
    instances = raceInfo.split(";")
    dist = 0
    for i in range(len(instances)):
        times, rate = instances[i].split(":")
        rate = float(rate)
        startTime, endTime = [float(i) for i in times.split("-")]
        if (i == len(instances) - 1):
            raceTime = endTime / 60
        tInterval = endTime - startTime
        dist += (tInterval * rate)
    truncRaceTime = "{:.1f}".format(raceTime)
    truncDist = "{:.1f}".format(dist)
    originalOrder.append(name)
    results[dist] = f'{name} {truncDist}m in {truncRaceTime}min'

keys = list(results.keys())
keys.sort(reverse=True)
placing = {i: results[i] for i in keys}

finalData = {}
for i, dist in enumerate(placing):
    place = i + 1
    abbrev = ""
    if place == 1:
        abbrev = "st"
    elif place == 2:
        abbrev = "nd"
    elif place == 3:
        abbrev = "rd"
    else:
        abbrev = "th"
    finalData[f'{results[dist]}'] = f'{place}{abbrev}' 
    
for name in originalOrder:
    for data in finalData:
        if (name in data):
            print(f'{data} ({finalData[data]})')
        