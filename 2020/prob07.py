with open("input.txt", "r") as file:
    data = [i for i in file.read().strip().split("\n")]

primaryColors = ["RED", "BLUE", "YELLOW"]

primToSec = {
    ("RED", "YELLOW"): "ORANGE",
    ("BLUE", "RED"): "PURPLE",
    ("BLUE", "YELLOW"): "GREEN"
}

for line in data:
    c1, c2 = line.split(" ")
    if (c1 == c2):
        print(c1)
    elif (c1 == "WHITE" or c2 == "WHITE"):
        colors = [c1, c2]
        print("LIGHT", end=" ")
        [print(i) for i in colors if i != "WHITE"]
    elif (c1 == "BLACK" or c2 == "BLACK"):
        colors = [c1, c2]
        print("DARK", end=" ")
        [print(i) for i in colors if i != "BLACK"]
    elif (c1 in primaryColors):
        key = (c1, c2)
        key = tuple(sorted(key))
        print(primToSec[key])
   
            
    