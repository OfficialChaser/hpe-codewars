length, width, est_area = input().split(" ")

length = int(length)
width = int(width)
est_area = int(est_area)

perimeter = 2 * length + 2 * width
area = length * width

print(f"{perimeter} {area} ", end = "")

if area >= est_area:
    print("ENOUGH SPACE")
else:
    print("NEED MORE SPACE")