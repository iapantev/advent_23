"""Day 6,
This time with chained lambda functions, not optimized but simple!
"""
from functools import reduce
from operator import mul

with open("./day_6/day_6_1.txt") as f:
    lines = f.readlines()
    times = list(map(int,lines[0].split(":")[1].split()))
    distances = list(map(int,lines[1].split(":")[1].split()))
    times2 = int("".join((lines[0].split(":")[1].split())))
    distances2 = int("".join((lines[1].split(":")[1].split())))

filterme = lambda dists, target: sum([d>target for d in dists])
dists_from_time  = lambda time: [(time-i)*i for i in range(time+1)]
producto = lambda ways: reduce(mul,ways)

print(f"Part 1: {producto([filterme(dists_from_time(time),distance) for time, distance in zip(times,distances)])}")
print(f"Part 2: {filterme(dists_from_time(times2),distances2)}")