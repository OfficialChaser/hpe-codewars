with open("input.txt", "r") as file:
    data = [i for i in file.read().strip().split('\n')]

found = False

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "A":
            print(f"Get out of there! Danger at ({x}, {y})")
            found = True

if not found:
    print("You are lucky. Get back to the office NOW!")