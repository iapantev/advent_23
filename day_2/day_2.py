"""Day 2,
Better late than never, starting from good values
"""

with open("./day_2/day_2_1.txt", "r") as f:
    lines = f.readlines()
    inpt = {}
    for i,line in enumerate(lines):
        picks = line.strip().split(":")[1]
        picks = picks.replace(";", ",").split(",")
        inpt[i+1] = {
            "red" : 0,
            "green" : 0,
            "blue" : 0}
        for pick in picks:
            subpick = pick.strip().split(" ")
            if inpt[i+1][subpick[1]] < int(subpick[0]):
                inpt[i+1][subpick[1]] = int(subpick[0])

def part_1(inpt:dict) -> int:
    total = 0
    for game, maxs in inpt.items():
        if 0< maxs["red"] <= 12 and 0< maxs["green"] <= 13 and maxs["blue"] <= 14:
            total += game
    return total

def part_2(inpt:dict) -> int:
    total = 0
    for game,maxs in inpt.items():
        total += maxs["red"]*maxs["green"]*maxs["blue"]
    return total

if __name__ == "__main__":
    print(f"Part 1: {part_1(inpt)}")
    print(f"Part 2: {part_2(inpt)}")