from functools import reduce
with open("./day_14/day_14_1.txt") as f:
    data = f.readlines()

countO = lambda x: x=="O"
def sort_or_skip(what):
    if len(what)>0:
        return "".join(sorted(what,key=lambda x: ord(x),reverse=True))
    else:
        return ""

# Glorious generators
def part1(data):
    # Transpose the input (rotate 90 CCW)
    col_order = list(map("".join,list(map(list,zip(*data)))))
    # Sort by the symbols (excluding #)
    sorted_cols = ["#".join(sort_or_skip(i) for i in col.split("#")) for col in col_order]
    # Transpose back to normal order
    row_order = list(map("".join,list(map(list,zip(*sorted_cols)))))
    # Add up all the weighted O's over all the rows
    total = sum(sum(list(map(countO,row)))*(len(data)-idx) for idx,row in enumerate(row_order))
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

def part2(data):
    """
    - Keep doing cycles until the result stops changing for several """
    pass

if __name__ == "__main__":
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")