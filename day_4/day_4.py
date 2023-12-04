"""Day 4
Warmed up - let's see if it makes a difference.
It does indeed, but still writing python with a C.
"""

with open("./day_4/day_4_1.txt","r") as f:
    lines = f.readlines()
    inpt = []
    for lidx, line in enumerate(lines):
        temp = {
            "win_nums" : {},
            "my_nums" : []
        }
        wins = list(map(int,line.replace(":","|").split("|")[1].split()))
        mine = list(map(int,line.replace(":","|").split("|")[2].split()))
        for win in wins:
            temp["win_nums"][win] = temp["win_nums"].get(win,0) + 1
        temp["my_nums"] = mine
        inpt.append(temp)

def part_1(inpt):
    total = 0
    for card in inpt:
        points = 0
        for my_num in card["my_nums"]:
            points += my_num in card["win_nums"]
        total += 2**(points-1) if points>=1 else 0
    return total

def part_2(inpt):
    copies = [1]*len(inpt)
    pts = []
    for idx, card in enumerate(inpt):
        points = 0
        for my_num in card["my_nums"]:
            points += my_num in card["win_nums"]
        result = 2**(points-1) if points>=1 else 0
        if points>0:
            for point in range(1,points+1):
                if idx+point<len(inpt):
                    copies[idx+point] += copies[idx]
        pts.append(result*copies[idx])
    return sum(copies)

if __name__ == "__main__":
    print(f"Part 1: {part_1(inpt)}")
    print(f"Part 2: {part_2(inpt)}")
