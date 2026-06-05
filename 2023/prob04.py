charToFind = input()
s = input()

for char in s:
    if (charToFind == char):
        index = (s.index(char))
        break

print(f'{charToFind} is at index: {index}')