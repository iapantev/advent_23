from operator import __eq__
with open("./day_14/test_14_1.txt") as f:
    data = f.readlines()
    data = [i.strip() for i in data]

countO = lambda x: x=="O"
def sort_or_skip(what,reverse_sort=True):
    if len(what)>0:
        return "".join(sorted(what,key=lambda x: ord(x),reverse=reverse_sort))
    else:
        return ""

# Glorious generators
def part1(data):
    total = sum(sum(list(map(countO,row)))*(len(data)-idx) for idx,row in enumerate(north(data)))
    return total

def north(data):
    # Transpose the input (rotate 90 CCW)
    col_order = list(map("".join,list(map(list,zip(*data)))))
    # Sort by the symbols (excluding #)
    sorted_cols = ["#".join(sort_or_skip(i) for i in col.split("#")) for col in col_order]
    # Transpose back to normal order
    row_order = list(map("".join,list(map(list,zip(*sorted_cols)))))
    # Add up all the weighted O's over all the rows
    return row_order

def south(data):
    # Transpose the input (rotate 90 CCW)
    col_order = list(map("".join,list(map(list,zip(*data)))))
    # Sort by the symbols (excluding #)
    sorted_cols = ["#".join(sort_or_skip(i,False) for i in col.split("#")) for col in col_order]
    # Transpose back to normal order
    row_order = list(map("".join,list(map(list,zip(*sorted_cols)))))
    return row_order

def west(data):
    sorted_cols = ["#".join(sort_or_skip(i) for i in col.split("#")) for col in data]
    return sorted_cols

def east(data):
    sorted_cols = ["#".join(sort_or_skip(i,False) for i in col.split("#")) for col in data]
    return sorted_cols

def check_cycle(data,len_cycle):
    return data[-len_cycle:]==data[-2*len_cycle:-len_cycle]

def part2(data):
    """
    - Keep doing cycles until we find a cycle """
    i,score_current = 1,0
    score_history = []
    current = data
    while i<150:
        current = east(south(west(north(current))))
        score_current = sum(sum(list(map(countO,row)))*(len(data)-idx) for idx,row in enumerate(current))
        score_history.append(score_current)
        if i>2:    
            for cycle_len in range(len(score_history)//2+1,2,-1):
                if check_cycle(score_history,cycle_len) and cycle_len>2:
                    offset = i-2*(cycle_len)
                    print(f"Offset = {offset}; Cycle len = {cycle_len}")
                    for idx,core in zip(range(offset-2,offset+cycle_len*2),score_history[offset-2:offset+cycle_len*2]):
                        print(idx,core,sep=" : ")
                    print(i-2*cycle_len-offset)
                    return score_history[int(offset+(1e9-offset+1)%(cycle_len-1))]
        i+=1
    return 0

if __name__ == "__main__":
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")