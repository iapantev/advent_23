"""Day 6,
This time with chained lambda functions, not optimized but simple!
But WITH MATH solution is O(1)
"""
from functools import reduce
from operator import mul
from math import sqrt, floor, ceil

with open("./day_6/day_6_1.txt") as f:
    lines = f.readlines()
    times = list(map(int,lines[0].split(":")[1].split()))
    distances = list(map(int,lines[1].split(":")[1].split()))
    times2 = int("".join((lines[0].split(":")[1].split())))
    distances2 = int("".join((lines[1].split(":")[1].split())))

def solve(ct,cd):
    x1 = (ct-sqrt(ct**2-4*cd))/2 
    diff = sqrt(ct**2-4*cd)
    if abs(round(x1)-x1)<1e-8 and abs(round(diff)-diff)<1e-8:
        return int(diff-1)
    return ceil(diff) if x1-int(x1)>=0.5 else floor(diff)

filterme = lambda dists, target: sum([d>target for d in dists])
dists_from_time  = lambda time: [(time-i)*i for i in range(time+1)]
producto = lambda ways: reduce(mul,ways)

print(f"Part 1: {producto([filterme(dists_from_time(time),distance) for time, distance in zip(times,distances)])}")
print(f"Part 1 (math) :  {producto([solve(time,distance) for time,distance in zip(times,distances)])}")

print(f"Part 2: {filterme(dists_from_time(times2),distances2)}")
print(f"Part 2 (math) : {solve(times2,distances2)}")
