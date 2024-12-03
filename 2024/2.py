def is_safe(r):
    diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]
    return ((all(d >= 1 for d in diffs) and all(d <= 3 for d in diffs))
        or (all(d <= -1 for d in diffs) and all(d >= -3 for d in diffs)))

def solve_first():
    with open('input.txt', 'rt') as f:
        reports = [list(map(int, l.strip().split(' '))) for l in f]
    return sum(is_safe(r) for r in reports)

def solve_second():
    with open('input.txt', 'rt') as f:
        reports = [list(map(int, l.strip().split(' '))) for l in f]
    safe_reports = 0
    for r in reports:
        if is_safe(r):
            safe_reports += 1
            continue
        for i in range(len(r)):
            if is_safe(r[:i] + r[i + 1:]):
                safe_reports += 1
                break
    return safe_reports

        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()