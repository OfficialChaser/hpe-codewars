with open("input.txt", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

# Getting string to check
givenStr = data[0]

# Places to store info
typingKey = {}
checkingWords = []

lettersStr = data[4]
letterKeys = lettersStr.split(";")

# Append to typingKey dict (d is data, don't wanna use "data" as a var twice tho)
for d in letterKeys:
    letter, neighboringLetters = [i.lower() for i in d.split(":")]
    tNLetters = tuple(neighboringLetters.split(","))
    typingKey[letter] = tNLetters

# Finding the checking words and appending
canRead = True
lineNum = 5
while canRead:
    word = data[lineNum]
    if (word == "ZZZZZ"):
        canRead = False
    else:
        checkingWords.append(word)
        lineNum += 1

# Making a list of every word in string
wordsInStr = givenStr.split(" ")

finalStr = []

# Correcting misspelled words
for word in wordsInStr:

    # If word is correct, we don't gotta worry about it
    if word not in checkingWords:

        # Just used b/c I'm doing 2 loops at once, and
        # "break" will only break me out of one
        wordCorrected = False
        
        # Keeping track of what the original word was, don't
        # Wanna change 2 letters in the word and screw everything up
        origWord = word

        for i, letter in enumerate(word):
            # Made word a list so I could use the pop and insert functions
            word = list(word)

            if (wordCorrected):
                break
            # Getting tuple from the dictionary (letters to check)
            lettersToCheck = typingKey[letter]

            for cLetter in lettersToCheck:
                # Pop and insert and you got a new version of the word
                word.pop(i)
                word.insert(i, cLetter)
                newWord = ""
                for ch in word:
                    newWord += ch

                # Check again for correct word
                if newWord in checkingWords:
                    wordCorrected = True
                    finalStr.append(newWord)
                    break
            
            word = origWord
    else:
        finalStr.append(word)
            
# Printing each word in corrected string
for w in finalStr:
    print(w, end=" ")

print()