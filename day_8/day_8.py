"""
Day 8
A little bit of math lets you go a short way
Part 2 is not fully robust, but works for the sample
"""
from functools import reduce

# Read the input and make our own "map"
with open("./day_8/day_8_1.txt") as f:
    lines = f.readlines()
    directions = lines[0].strip()
    data = [line.strip().replace(" ","").replace("=",",").replace("(","").replace(")","") for line in lines[2:]]
nodes = {}
for i in data:
    node, left, right = i.split(",")
    nodes[node] = {"R" : right,
                   "L" : left}

# For a simple problem the brute force way will do
def part1(start,end,nodes,directions):
    current = start
    i=0
    while current != end:
        current = nodes[current][directions[i%len(directions)]]
        i+=1
    return i

# Some basic maths
def gcd(a,b):
    """Return the greatest common denominator of two numbers

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        Greatest common denominator
    """    
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    """Returns the lowest common multiple of two numbers

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        Lowest common multiple of the two numbers
    """    
    return (a*b)//gcd(a,b)

def multiplelcm(*args):
    """Returns the lowest common multiple for multiple numbers

    Returns
    -------
    int
        Lowest common multiple of the inputs
    """    
    return reduce(lcm,args)

# Brute forcing will not do here, but modulos are our friend
def part2(nodes, directions):
    current = [node for node in nodes.keys() if node[-1]=="A"]
    print(current)
    checkz = lambda x: x[-1]=="Z"
    storage = [False]*len(current)
    i=0
    while True:
        current = [nodes[start][directions[i%len(directions)]] for start in current]
        i += 1
        storage = [i if (~stor and check) else stor for stor,check in zip(storage,list(map(checkz,current)))]
        if all(storage):
            break
    return multiplelcm(*storage)

if __name__ == "__main__":
    print(f"Part 1: {part1(start='AAA',end='ZZZ',nodes=nodes,directions=directions)}")
    print(f"Part 2: {part2(nodes=nodes, directions=directions)}")