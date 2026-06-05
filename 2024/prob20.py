ended = False

while not ended:
    line = input()

    if line == "END":
        ended = True
        continue

    sections = line.split(", ")
    print(f"{sections[0]}\n{sections[1]}")
    print(f"{sections[2]}, {sections[3]} {sections[4]}")
    print()