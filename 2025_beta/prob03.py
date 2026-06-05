import math
end = False

while not end:
    line = input()

    if line == "END":
        end = True
        continue
    
    num1, num2, operator, expected = line.split(" ")
    num1, num2, expected = float(num1), float(num2), float(expected)

    res = 0.0
    correct = False
    op = ""
    if operator == "ADD":
        op = "+"
        res = num1 + num2

    if operator == "SUBTRACT":
        op = "-"
        res = num1 - num2

    if operator == "MULTIPLY":
        op = "*"
        res = num1 * num2

    if operator == "DIVIDE":
        op = "/"
        res = num1 / num2
        res = math.floor(res * 10) / 10

    if res == expected:
        correct = True
        

    if correct:
        print(f"{res:.1f} is correct for {num1} {op} {num2}")
    else:
        print(f"{num1} {op} {num2} = {res:.1f}, not {expected}")