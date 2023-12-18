with open("./day_13/test_13_1.txt") as f:
    patterns = [[]]
    data = f.readlines()
    for line in data:
        if line=="\n":
            patterns.append([])
        else:
            patterns[-1].append(line.strip())

def find_reflection(pattern):
    for idx in range(1,len(pattern[0])-2):
        if idx>(len(pattern[0])-1)/2:
            left = 2*idx-len(pattern[0])
            right = len(pattern[0])

        else:
            left = 0
            right = min(2*idx+1,len(pattern[0]))
            # print(f"Reflection at {idx+1}")
        if all([row[left:idx+1][::-1]==row[idx+1:right+1] for row in pattern]):
            # for row in pattern:
            #     print(f"Checking: {row[idx:left:-1]} | {row[idx+1:right]}")
            return idx+1
    return 0    

def part1(patterns):
    total = 0
    ref_total = 0
    for ip,pattern in enumerate(patterns):
        cols,rows=0,0
        cols = find_reflection(pattern)
        rows = find_reflection(list(map("".join,list(map(list,zip(*pattern)))[::-1])))
        total+= cols+(rows*100)#cols if cols>rows else rows*100
        ref_total += cols>0 or rows>0
    print(f"Patterns checked {ip+1}, reflections {ref_total}")
    return total

def flip(pattern):
    return list(map("".join,list(map(list,zip(*pattern)))[::-1]))

# def printi(pattern,idx):
#     for row in pattern:
        # if idx>len(pattern)

if __name__ == "__main__":
    print(f"Part 1 : {part1(patterns)}")
    # print(*patterns[0],sep='\n')
    # print(*flip(patterns[0]),sep='\n')