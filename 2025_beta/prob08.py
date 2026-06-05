with open("input.txt", "r") as file:
    data = [i for i in file.read().strip().split('\n')]

data = data[1:]
for line in data[::-1]:
    print(line)