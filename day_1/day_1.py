with open("./day_1/day_1_1.txt", "r") as f:
    lines = f.readlines()

with open("./day_1/test_1_2.txt", "r") as f:
    test2 = f.readlines()

with open("./day_1/test_1_1.txt","r") as f:
    test1 = f.readlines()

# Map word to digits
mapping = {"one" : "1",
           "two" : "2",
           "three" : "3",
           "four" : "4",
           "five" : "5",
           "six" : "6",
           "seven" : "7",
           "eight" : "8",
           "nine" : "9"}
# Digit words to not remove 
replacing = {
    "one" : "oonee",
    "two" : "ttwoo",
    "three" : "tthreee",
    "four" : "ffourr",
    "five" : "ffivee",
    "six" : "ssixx",
    "seven" : "ssevenn",
    "eight" : "eeightt",
    "nine" : "nninee"
}
def part_1(lines: list) -> int:
    total = 0
    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        total += 10*digits[0] + digits[-1]
    return total

def part_2(lines: list, mapping: dict, replacing: dict) -> int:
    total = 0
    for line in lines:
        for word, newword in replacing.items():
            line = line.replace(word,newword)
        for word, digit in mapping.items():
            line = line.replace(word, digit)
        digits = [int(c) for c in line if c.isdigit()]
        total += 10*digits[0] + digits[-1]
    return total

if __name__ == "__main__":
    assert part_1(test1)==142, "Part 1 failed."
    print(f"Part 1: {part_1(lines)}")
    assert part_2(test2,mapping,replacing)==281, "Part 2 failed."
    print(f"Part 2: {part_2(lines, mapping, replacing)}")