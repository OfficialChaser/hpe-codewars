import sys

with open('prob4.in', 'r') as file:
    data = [i for i in file.read().strip().split('\n')]

for line in data:
    print(line)

print()

for line in data[::-1]:
    print(line)

