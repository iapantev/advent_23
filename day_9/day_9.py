from functools import reduce
from operator import __eq__

with open("./day_9/day_9_1.txt") as f:
    data = f.readlines()
    nums = [list(map(int,line.split())) for line in data]

# Glorious recursion
def recurse(nums):
    diffs = [int(j-i) for i,j in zip(nums[:-1],nums[1:])]
    if reduce(__eq__,nums) and diffs[-1]==0:
        return nums[-1]
    else:
        return recurse(diffs)+nums[-1]

def recurse2(nums):
    diffs = [-int(i-j) for i,j in zip(nums[:-1],nums[1:])]
    # print(f"{nums[::-1]} -> {diffs[::-1]}")
    if all(list(map(__eq__,diffs,[0]*len(diffs)))):
        return nums[-1]
    else:
        return nums[-1]+recurse(diffs)

def part1(nums):
    return sum([recurse(row) for row in nums])

def part2(nums):
    return sum([recurse2(row[::-1]) for row in nums])

if __name__ == "__main__":
    print(f"Part 1: {part1(nums)}")
    print(f"Part 2: {part2(nums)}")

    # print([recurse(row[::-1]) for row in nums])