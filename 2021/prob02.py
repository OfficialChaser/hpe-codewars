import math

h, r = (input().split(" "))
h = float(h)
r = float(r)
pi = 3.1415926536
v = pi * r * r * h
print("{:.2f}".format(v))