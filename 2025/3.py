def max_joltage(digits):
    max_digit_pos = len(digits) - 2
    for i in range(max_digit_pos - 1, -1, -1):
        if digits[i] >= digits[max_digit_pos]:
            max_digit_pos = i
    max_second_digit_pos = max_digit_pos + 1
    for i in range(max_second_digit_pos + 1, len(digits)):
        if digits[i] > digits[max_second_digit_pos]:
            max_second_digit_pos = i
    return 10 * digits[max_digit_pos] + digits[max_second_digit_pos]

def solve_first():
    total = 0
    with open('input.txt', 'rt') as f:
        for line in f:
            digits = [int(s) for s in line.strip()]
            mj = max_joltage(digits)
            print(line, mj)
            total += mj
    return total


def leftmost_largest_pos(digits, l, r):
    max_digit_pos = r - 1
    for i in range(r - 2, l - 1, -1):
        if digits[i] >= digits[max_digit_pos]:
            max_digit_pos = i
    return max_digit_pos

def max_joltage(digits, batteries_count):
    joltage = 0
    l = 0
    r = len(digits) - batteries_count + 1
    for b in range(batteries_count):
        max_digit_pos = leftmost_largest_pos(digits, l, r)
        joltage = 10 * joltage + digits[max_digit_pos]
        l = max_digit_pos + 1
        r += 1
    return joltage


def solve_second():
    total = 0
    with open('input.txt', 'rt') as f:
        for line in f:
            digits = [int(s) for s in line.strip()]
            mj = max_joltage(digits, 12)
            total += mj
    return total

def main():
    print(solve_second())

if __name__ == '__main__':
    main()
