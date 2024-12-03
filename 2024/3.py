import re

def solve_first():
    with open('input.txt', 'rt') as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', line)
        for m in matches:
            total += int(m[0]) * int(m[1])
    return total
    

def solve_second():
    with open('input.txt', 'rt') as f:
        lines = f.readlines()
    total = 0
    enabled = True
    for line in lines:
        matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))", line)
        for m in matches:
            if m[2] == "do()":
                enabled = True
            elif m[3] == "don't()":
                enabled = False
            elif enabled:
                total += int(m[0]) * int(m[1])
    return total

        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()