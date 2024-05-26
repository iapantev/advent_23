"""Day 17:
IDEA : Dynamic programming, with limited lookback (i.e. two squares)
Keep the minimum heat loss required to reach each square (considering rules).
Return the heat loss at the end.
Tweak needed for the "straight" distance travelled to get to the given tile.
E.g. each tile contains:
(min (heatloss), lastdir, twoinline) x4 for the four ways we can reach the tile (top,right,bottom,left)
"""
from collections import namedtuple
step = namedtuple("Step",("loss", "dirCount")) # dirCount keeps info on last directions
# tile = namedtuple("Step")

with open("./day_17/day_17_1.txt") as f:
    data = [list(map(int,i.strip())) for i in f.readlines()]
    target = (len(data[0])-1,len(data)-1)
    #Worst case
    maxloss = sum(map(sum,data))

def addLoss():
    pass

def part1(data:list[list]) -> int:
    losses = [maxloss]
    while x<target[0] and y<target[1]:
        if x==0 and y==0:
            losses[y][x] = step(0,0)
        elif x==0 and y>0:
            losses[y][x] = step(1,2) #TODO: this is random
        pass

if __name__ == "__main__":
    print(f"Part 1: {part1(data)}")
        
