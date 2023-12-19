from functools import reduce
with open("./day_15/day_15_1.txt") as f:
    alldata = f.readline().strip().split(',')

def hash(data: str,start=0) -> int:
    fn = lambda x0,x: ((ord(x)+x0)*17)%256
    total = reduce(fn,data,0)
    return total

def part1(alldata: list[str]) -> int:
    return sum(map(hash,alldata))

def part2(alldata):
    hashmap = [{} for _ in range(256)]
    for data in alldata:
        if "-" in data:
            box,lens = hash(data.split("-")[0]), data.split("-")[0]
            hashmap[box].pop(lens,0)
        elif "=" in data:
            box,lens,focus = hash(data.split("=")[0]),data.split("=")[0],int(data.split("=")[1])
            if lens in hashmap[box]:
                hashmap[box][lens] = (focus,hashmap[box][lens][1])
            else:
                if len(hashmap[box])==0:
                    hashmap[box][lens] = (focus,1)
                else:
                    maxslot = max(hashmap[box].values(),key=lambda x: x[1])
                    hashmap[box][lens] = (focus,maxslot[1]+1)
    total = sum(sum((boxID+1)*lens[0]*(slot+1) for slot,lens in enumerate(sorted(box.values(),key=lambda x: x[1]))) for boxID,box in enumerate(hashmap))
    return total

if __name__ == "__main__":
    print(f"Part 1: {part1(alldata)}")
    print(f"Part 2: {part2(alldata)}")