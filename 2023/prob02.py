end = False
answers = {}

while not end:
    num = int(input())
    if (num == 0):
        end = True
    elif (num % 4 == 0):
        q = int(num / 4)
        answers[num] = q

for key, value in answers.items():
    print(f"{key}/4 = {value}")