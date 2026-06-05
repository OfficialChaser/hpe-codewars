end = False

while not end:
    eqn = input()
    if eqn == "END":
        end = True
        continue

    n1, ending = eqn.split("+")
    n1 = int(n1)

    n2, sum = [int(i) for i in ending.split("=")]

    if n1 + n2 == sum:
        print("CORRECT")
        continue

    print(f"WRONG: {n1}+{n2}={n1+n2}")