import sys

with open('prob3.in', 'r') as file:
    data = [i for i in file.read().strip().split('\n')]

foundPigeon = False

y = 0
for line in data:
    x = 0
    for char in line:
        if char == "P":
            print(f"Ace, move fast, pigeon is at ({x},{y})")
            foundPigeon = True
            break
        x += 1
    y += 1

if (foundPigeon == False):
    print("No pigeon, try another map, Ace")