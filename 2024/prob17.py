categories = {}
numOfCategories = int(input())

for _ in range(numOfCategories):
    name, words = input().split("=")
    cWords = words.split(",")
    categories[name] = cWords

canRead = True

while canRead:
    line = input()
    if (line != "THE END."):
        for category in categories:
            string = f'<{category.upper()}>'
            if (string in line):
                line = line.replace(category.upper(), categories[category][0])
                categories[category].pop(0)

        line = line.replace("<", "")
        line = line.replace(">", "")            
        print(line)
            
    else:
        canRead = False