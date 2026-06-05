word_list = [i for i in input().split(" ")]
chemical = word_list[0].rstrip("(")

print(chemical)

top_line = []
bottom_line = []

for char in chemical:
    if char.isalpha():
        top_line.append(char)
        bottom_line.append(" ")
    else:
        top_line.append(" ")
        bottom_line.append(char)

[print(i, end="") for i in top_line]
print()
[print(i, end="") for i in bottom_line]
print()