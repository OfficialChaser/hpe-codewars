with open('input.txt', 'r') as file:
    data = [i for i in file.read().strip().split('\n')]

dates = []
dups = []
for line in data:
    if line != line[0]:
        dates.append(line[:5])

for date in dates:
    if (dates.count(date) > 1 and date not in dups):
        dups.append(date)

print(len(dups))
if (len(dups) > 0):
    [print(date, end=" ") for date in dups]
else:
    print('duplicates: None')