"""
Day 10
No avoiding graphs anymore
"""

with open("./day_10/test_10_1.txt") as f:
    data = list(map(str.strip,f.readlines()))
    grid_w,grid_h = len(data[0]),len(data)

# Construct the graph
# Find the loop!
# BFS search to find the furthest node from the start

def check_connection(chr,col,row):
    if chr=="|":
        return [(col,row-1),(col,row+1)]
    elif chr=="-":
        return [(col-1,row),(col+1,row)]
    elif chr=="L":
        return [(col,row-1),(col+1,row)]
    elif chr=="J":
        return [(col,row-1),(col-1,row)]
    elif chr=="7":
        return [(col,row+1),(col-1,row)]
    elif chr=="F":
        return [(col,row+1),(col+1,row)]
    return [(-1,-1)]


# Make connectivity list or array
connections = [[False]*grid_w]*grid_h
start = []
for ridx,row in enumerate(data):
    for cidx, chr in enumerate(row):
        cons = check_connection(chr,ridx,cidx)
        if cons==None and chr=="S":
            start = [cidx,ridx]
        for x,y in cons:
            if grid_w-1>=x>=0 and grid_h-1>=y>=0:
                connections[y][x] = True

print(connections)
