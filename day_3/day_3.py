"""Day 3
Early start, maybe too early.
When counting by initiating new, better to initiate more and filter, than initiate less and not know it.
"""

from functools import reduce
from operator import mul

with open("./day_3/day_3_1.txt","r") as f:
    lines = [i.strip() for i in f.readlines()]
    numbs = [[None,None,0,[]]]
    symbs = []
    for lidx,line in enumerate(lines):
        for cidx,char in enumerate(line):
            if char.isdigit():
                numbs[-1][0] = lidx
                numbs[-1][3].append(char)
                if numbs[-1][1] == None:
                    numbs[-1][1] = cidx
                else:
                    numbs[-1][2] += 1
            else:
                numbs.append([None, None, 0,[]])
                if char != ".":
                    symbs.append([lidx,cidx,char])
    numbs = [i for i in numbs if i[0]!=None]

def part1(symbs, numbs) -> int:
    total = 0
    used = set()
    for symb in symbs:
        for idx,numb in enumerate(numbs):
            if idx not in used:
                if numb[0]-1 <= symb[0] <= numb[0]+1:
                    if ((numb[1] <= symb[1]) and (numb[1]+numb[2] >= symb[1]-1)) or (numb[1] == symb[1]+1):
                        total += int("".join(numb[3]))
                        used.add(idx)
    return sum((int("".join(numbs[i][3])) for i in used))

def part2(symbs, numbs) -> int:
    gears = []
    for symb in symbs:
        if symb[2]=="*":
            gears.append([])
            for numb in numbs:
                if numb[0]-1 <= symb[0] <= numb[0]+1:
                    if ((numb[1] <= symb[1]) and (numb[1]+numb[2] >= symb[1]-1)) or (numb[1] == symb[1]+1):
                        gears[-1].append(int("".join(numb[3])))
    return sum([reduce(mul,i) for i in gears if len(i)==2])

if __name__ == "__main__":
    print(f"Part 1: {part1(symbs,numbs)}")
    print(f"Part 2: {part2(symbs,numbs)}")