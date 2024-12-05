class UpdateValidator:
    def __init__(self):
        self._rules = set()
        self._updates = []
        with open('input.txt', 'rt') as f:
            while True:
                l = f.readline().strip()
                if len(l) == 0:
                    break
                self._rules.add(tuple(map(int, l.split('|'))))
            for l in f:
                self._updates.append(list(map(int, l.split(','))))

    def update_is_correct(self, update):
        for i in range(len(update) - 1):
            for j in range(i, len(update)):
                if (update[j], update[i]) in self._rules:
                    return False
        return True
    
    def aggregate_correct_updates(self):
        return sum(u[len(u) // 2] for u in self._updates if self.update_is_correct(u))
    
    def fix_update(self, update):
        while not self.update_is_correct(update):
            for i in range(len(update) - 1):
                for j in range(i, len(update)):
                    if (update[j], update[i]) in self._rules:
                        update[i], update[j] = update[j], update[i]
        return update

    def aggregate_incorrect_updates(self):
        total = 0
        for u in self._updates:
            if self.update_is_correct(u):
                continue
            self.fix_update(u)
            total += u[len(u) // 2]
        return total


def solve_first():
    update_validator = UpdateValidator()
    return update_validator.aggregate_correct_updates()


def solve_second():
    update_validator = UpdateValidator()
    return update_validator.aggregate_incorrect_updates()
        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
