chars = input()

num_indexes = []

letters = []
numbers = []

for i, char in enumerate(chars):
    if char.isnumeric():
        num_indexes.append(i)
        numbers.append(char)
    else:
        letters.append(char)

letters.sort()
numbers.sort()

output = ""

for i in range(len(chars)):
    if i in num_indexes:
        output += numbers[0]
        numbers.pop(0)
    else:
        output += letters[0]
        letters.pop(0)

print(output)