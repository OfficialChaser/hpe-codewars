num_of_students = int(input())

for i in range(num_of_students):
    total_months = 0
    name, years, months = input().split(" ")
    total_months = int(years) * 12 + int(months)
    print(f"{name} {300 - total_months}")