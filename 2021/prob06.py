_ = input()
s = input()

message = ""
for char in s:
    if (char.isalpha()):
        char = ord(char)
        char -= 5
        if (char < 65 or char > 90 and char < 97):
            char += 26
        char = chr(char)
        message += char
    else:
        message += char

print(message)