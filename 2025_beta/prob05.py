c = input()
s = input()
n = s.index(c)
print(s[n + 1:] + s[n] + s[:n])

