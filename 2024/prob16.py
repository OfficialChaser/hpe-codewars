found = False
nums = []

while not found:
    num = int(input())
    if num == 0:
        found = True
    else:
        nums.append(num)

nums_no_dups = list(set(nums))

first = 0
first_freq = 0
second = 0
second_freq = 0

for num in nums_no_dups:
    freq = nums.count(num)

    if freq > first_freq:
        if first_freq > second_freq:
            second_freq = first_freq
            second = first

        first = num
        first_freq = freq

    elif freq > second_freq:
        second = num
        second_freq = freq

print(f"Trending: {first} [{first_freq} count]")
print(f"Second Place: {second} [{second_freq} count]")