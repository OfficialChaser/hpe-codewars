# y = mx + b
m, b, grid_size = [int(i) for i in input().split(" ")]
print(f"y = {m}x+{b}")

for y in range(grid_size, 0, -1):
    # Create y-axis number string
    axis_num = str(y)
    if y < 10:
        axis_num = "0" + str(y)

    # Horizontal line edge case
    if m == 0:
        if y == b:
            print(axis_num[0], end="")
            for i in range(grid_size + 1):
                print("#", end=" ")
        else:
            print(axis_num, end="")
        print()
        continue

    # Finding x, checking if it's an integer and in bounds, if so there is a hashtag
    x = (y - b) / m
    has_hashtag = x.is_integer() and (0 <= x <= grid_size)

    # Checking for y int (x will be 0)
    if has_hashtag and int(x) == 0:
        # If so, print the axis number differently
        print(axis_num[0] + "#")
        continue
    else:
        print(axis_num, end="")

    # Print hashtag at appropriate spot
    if has_hashtag and y != 0:
        for i in range(int(x) * 2 - 1):
            print(" ", end="")
        print("#")
    else:
        print()

# Print the x-axis numbers
x_axis_str = ""
# Changes if there is a point at (0, 0)
if b == 0:
    x_axis_str += "0#"
else:
    x_axis_str += "00"
    
for num in range(1, grid_size + 1):
    axis_num = str(num)
    if num < 10:
        axis_num = "0" + str(num)
    x_axis_str += axis_num
print(x_axis_str)