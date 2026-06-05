with open("input.txt", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

conj = data[0].lower()
ingredients = []
for i in range(len(data) - 1):
    ingredient = data[i + 1]
    ingredients.append(ingredient)

if (len(ingredients) == 1):
    print(ingredients[0])
elif (len(ingredients) == 2):
    print(f'{ingredients[0]} {conj} {ingredients[1]}')
else:
    for ing in ingredients[:-1]:
        print(ing, end=", ")
    print(f'{conj} {ingredients[-1]}')