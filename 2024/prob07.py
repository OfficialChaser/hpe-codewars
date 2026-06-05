line = input()
output = ""

counter = 1
current_char = ""

for char in line:

    if char != current_char:

        # Check if there is 4 in a row
        if counter == 4:
            output += current_char

        # Resetting current character
        current_char = char
        counter = 1
        continue
    
    # Increment counter if there is a duplicate
    counter += 1

if output:
    print(output)
else:
    print("No Four of a Kind")