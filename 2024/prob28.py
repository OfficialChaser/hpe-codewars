# INCOMPLETE - Will get a memory error if cities are above like 13 or so
import math
import csv
from itertools import *

# Degrees to radians
def deg_to_rad(deg):
    return deg * 3.1415926 / 180

# Read input
with open("input.txt", "r") as file:
    cities = [i for i in file.read().strip().split('\n')]
cities = cities[1:]

# Read csv file
city_data = {}
with open("student_datasets/files/cities.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        city = row[0]
        if city in cities:
            city_data[city] = [float(row[2]), float(row[3])]


# Calculate distance
def calc_distance(cities, s_dist=0, end_quicker=False):
    dist = 0
    for i in range(len(cities) - 1):
        city1, city2 = cities[i:i+2]
        lat1, lon1 = [deg_to_rad(i) for i in city_data[city1]]
        lat2, lon2 = [deg_to_rad(i) for i in city_data[city2]]
        dist += math.acos((math.sin((lat1)) * math.sin((lat2))) + (math.cos((lat1)) * math.cos((lat2))) * (math.cos((lon2) - (lon1)))) * 6371
        if end_quicker and dist > s_dist:
            return dist
    return math.trunc(dist)

# Print solution
def print_solution(cities, distance, title="ROUTE"):
    print(title + ": ", end="")
    [print(i, end=":") for i in cities[:len(cities) - 1]]
    print(cities[len(cities) - 1], end=" = ")
    print(distance)

shortest_distance = calc_distance(cities)
print_solution(cities, shortest_distance)

re_route = cities
for route in list(permutations(cities)):
    d = calc_distance(route, shortest_distance, True)
    if d < shortest_distance:
        re_route = route
        shortest_distance = d

if re_route == cities:
    print("OPTIMUM")
else:
    print_solution(re_route, shortest_distance, "RE-ROUTE")