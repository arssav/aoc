from collections import deque

class Machine:
    def __init__(self, lights: list[int], buttons: list[list[int]], joltage: list[int]):
        self.target_lights = lights
        self.buttons = buttons
        self.target_joltage = joltage
        self.num_lights = len(lights)


    def neighbors(self, lights: list[int]):
        for button in self.buttons:
            new_lights = lights[:]
            for index in button:
                new_lights[index] ^= 1
            yield new_lights

    def turn_on(self) -> int:
        lights = [0] * self.num_lights
        q = deque()
        dist = {tuple(lights): 0}

        q.append(lights)

        while q:
            lights = q.popleft()
            d = dist[tuple(lights)]
            if lights == self.target_lights:
                return d
            for new_lights in self.neighbors(lights):
                new_lights_tuple = tuple(new_lights)
                if new_lights_tuple not in dist:
                    dist[new_lights_tuple] = d + 1
                    q.append(new_lights)
        return -1
    
    def min_presses(self, buttons: list[list[int]], target_joltage: list[int]) -> int:
        if all(j == 0 for j in target_joltage):
            return 0
        if len(buttons) == 0:
            return -1
        
        # Find the light that is targeted by the least number of buttons
        num_occurences = [0] * len(target_joltage)
        for b in buttons:
            for i in b:
                num_occurences[i] += 1
        least_occuring_light = -1
        for i in range(len(target_joltage)):
            if num_occurences[i] == 0:
                if target_joltage[i] > 0:
                    return -1
                else:
                    continue
            if least_occuring_light == -1 or num_occurences[i] < num_occurences[least_occuring_light]:
                least_occuring_light = i
        assert least_occuring_light != -1


        # Iterate buttons which affect that light
        buttons_with_light = set([i for i in range(len(buttons)) if least_occuring_light in buttons[i]])
        assert len(buttons_with_light) > 0

        b = next(iter(buttons_with_light))

        max_b0_presses = min(target_joltage[i] for i in buttons[b])
        min_found = -1
        for p in range(max_b0_presses + 1):
            new_target_joltage = target_joltage[:]
            for i in buttons[b]:
                new_target_joltage[i] -= p
            if any(j < 0 for j in new_target_joltage):
                continue
            res = self.min_presses(buttons[:b] + buttons[b + 1:], new_target_joltage)
            if res != -1:
                total_presses = res + p
                if min_found == -1 or total_presses < min_found:
                    min_found = total_presses

        return min_found

    def configure_joltage(self) -> int:
        return self.min_presses(self.buttons, self.target_joltage)    


class Factory:
    def __init__(self, filename):
        self.machines: list[Machine] = []
        with open(filename, 'rt') as f:
            for line in f:
                i = line.find(']')
                lights = [1 if c == '#' else 0 for c in line[1:i]]
                j = line.find('{')
                buttons = []
                for button_pattern in line[i + 2 : j - 1].split(' '):
                    buttons.append(list(map(int, button_pattern[1 : -1].split(','))))
                joltage = list(map(int, line[j + 1 : -2].split(',')))
                self.machines.append(Machine(lights, buttons, joltage))
    

    def solve_first(self):
        return sum(machine.turn_on() for machine in self.machines)
    
    def solve_second(self):
        total = 0
        for n, machine in enumerate(self.machines):
            j = machine.configure_joltage()
            print(f"Machine {n}: {j}")
            total += j
        return total

    
def main():
    factory = Factory("input.txt")
    print(factory.solve_second())

if __name__ == "__main__":
    main()
