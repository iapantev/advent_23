"""Day 12
Separate input by points, to show available spaces for groups
Check cases:
space > group; simple case => ways = space-group
complex case: maybe not needed
Greedy algo -> start with biggest group and biggest slot
OR BRUTE - with product of groups and slots
OR WEIRD REGEX"""

with open("./day_12/day_12_1.txt","w") as f:
    data = f.readlines()