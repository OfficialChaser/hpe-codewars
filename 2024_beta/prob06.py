charToFind = input()
found = False
while not found:
    file = input()
    if (file != "END"):
        with open(file, "r") as f:
            data = [i for i in f.read().strip().split('\n')]
        
        y = 0
        for line in data:
            x = 0
            for char in line:
                if (char == charToFind):
                    location = file.strip(".txt")
                    print(f"Found the ring! It was {location} at ({x}, {y})")
                    found = True
                x += 1
            y += 1
    else:
        break