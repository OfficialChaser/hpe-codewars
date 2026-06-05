chr1, chr2 = [i.lower() for i in input().split(" ")]

canRead = True
originalWords = []
newWords = []

output = {}
while canRead:
    word = input()
    if (word != "END"):
        originalWords.append(word)
        newWord = ""
        for char in word:
            char = char.lower()
            if (char == chr1):
                char = chr2
            elif (char == chr2):
                char = chr1
            newWord += char
        newWords.append(newWord)
    else:
        canRead = False

for i, word in enumerate(newWords):
    output[word] = originalWords[i]

keys = list(output.keys())
keys.sort()
sortedOutput = {i: output[i] for i in keys}

for key in sortedOutput:
    print(sortedOutput[key])