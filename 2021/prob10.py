canRead = True
tastyVillagers = []

while canRead:
    line = input()
    if (line != "END"):
        line = line.strip("Villager-")
        code, time, vpf = line.split(" ")
        vpf = float(vpf)
        hrs, mins = [float(i) for i in time.split(":")]
        protTime = hrs + (mins / 60) + ((vpf * 10) / 60)
        if (protTime < 17):
            tastyVillagers.append(code)
    else:
        canRead = False

if (len(tastyVillagers) > 0):
    codes = ""
    for i in range(len(tastyVillagers) - 1):
        codes += tastyVillagers[i] + ", "
    codes += tastyVillagers[-1]

    print(f"Villagers ({codes}) look tasty")
else:
    print("Blah, blah, blah, time to order delivery")