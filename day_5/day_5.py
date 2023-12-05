"""Day 5
Mappers, possibly functional solution
"""
from collections import namedtuple, deque
from itertools import chain

Mapper = namedtuple("Mapper",["dest", "source", "length"])
Mappers = []
Ranger = namedtuple("Ranger", ["min","max"])

class ranger():
    def __init__(self,start,length):
        self.min = start
        self.max = start+length
    def dif(self,other):
        pass

inputs = deque()


with open("./day_5/day_5_1.txt") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        if idx==0:
            inpt = list(map(int,line.split()[1:]))
        if idx>0 and line[0].isalpha():
            Mappers.append([])
        if idx>0 and line[0].isdigit():
            Mappers[-1].append(Mapper(*list(map(int,line.split()))))

# Simple solution for part 1
def check_range(inpt,Mapper):
    if Mapper.source <= inpt < Mapper.source + Mapper.length:
        return Mapper.dest + inpt - Mapper.source
    else:
        return None
    
def range_splitter(input_range, mapping_range):
    to_split = []
    split = []
    # No overlap -> input_range not split
    if input_range.max < mapping_range.min or mapping_range.max < input_range.min:
        to_split.append(input_range)
    elif input_range.min <= mapping_range.min:
        if mapping_range.max <= input_range.max:
            # new_ranges.append()
            pass

# Part 1 fine for small inputs
def part_1(inpt,Mappers):
    locations = []
    for seed in inpt:
        locations.append([seed])
        for maps in Mappers:
            res = [check_range(locations[-1][-1],mappi) for mappi in maps]
            res = [i for i in res if i!= None]
            res = res[0] if len(res)==1 else locations[-1][-1]
            locations[-1].append(res)
    return min([i[-1] for i in locations])

# Part 2 can take forever...BUT IT WILL WORK EVENTUALLY
def part_2(inpt,Mappers):
    range_inpt = [range(i,i+j) for i,j in zip(inpt[0::2],inpt[1::2])]
    mini = None
    for seed in chain(*range_inpt):
        locations = [seed]
        for maps in Mappers:
            res =[check_range(locations[-1],mappi) for mappi in maps]
            res = [i for i in res if i!= None]
            res = res[0] if len(res)==1 else locations[-1]
            locations.append(res)
        # print(locations)
        if mini!=None:
            mini = locations[-1] if locations[-1]<mini else mini
        else:
            mini = locations[-1]
    return mini

# With "RANGE MATH"
def part_2_ranges(inpt, Mappers):
    pass

if __name__ == "__main__":
    print(f"Part 1: {part_1(inpt,Mappers)}")
    # print(f"Part 2: {part_2(inpt,Mappers)}")
        