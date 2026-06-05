stopped = False

while not stopped:
    line = input()

    if line == "STOP":
        stopped = True
        continue

    output = []
    for char in line:
        output.append(char)
    
    for i, char in enumerate(output):
        if i == 0 or char != output[i - 1] or char.isalpha() == False:
            continue
        
        output.pop(i)
    
    for char in output:
        print(char, end="")
    
    print()