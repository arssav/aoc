class Computer:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self.A = int(f.readline().strip().split(': ')[1])
            self.B = int(f.readline().strip().split(': ')[1])
            self.C = int(f.readline().strip().split(': ')[1])

            f.readline()
            self._program = list(map(int, f.readline().strip().split(': ')[1].split(',')))

        self.output: list[int] = []
        self.A0 = self.A
        self.B0 = self.B
        self.C0 = self.C
    
    def combo_operand_value(self, operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C

    def process_instruction(self, opcode: int, operand: int):
        operand_value = None
        if opcode in (1, 3):
            operand_value = operand
        else:
            operand_value = self.combo_operand_value(operand)

        if opcode == 0: # adv
            self.A = self.A // (2 ** operand_value)
        elif opcode == 1: # bxl
            self.B = self.B ^ operand_value
        elif opcode == 2: # bst
            self.B = operand_value % 8
        elif opcode == 3: # jnz
            if self.A == 0:
                return None
            return operand_value
        elif opcode == 4: # bxc
            self.B ^= self.C
        elif opcode == 5: # out
            self.output.append(operand_value % 8)
        elif opcode == 6: # bdv
            self.B = self.A // (2 ** operand_value)
        elif opcode == 7: # cdv
            self.C = self.A // (2 ** operand_value)
        return None

    def compute(self, break_early=False):
        ins_pointer = 0
        while ins_pointer < len(self._program):
            opcode = self._program[ins_pointer]
            operand = self._program[ins_pointer + 1]
            jump = self.process_instruction(opcode, operand)
            if break_early and opcode == 5 and self.output[-1] != self._program[len(self.output) - 1]:
                return self.output

            if jump is not None:
                ins_pointer = jump
            else:
                ins_pointer += 2

        return self.output
    
    def reset(self, A):
        self.A = A
        self.B = self.B0
        self.C = self.C0
        self.output = []
            
    def find_quine_smart(self):
        settled_suffix = 0
        settled_3bytes = 0
        while True:
            mask = 0
            while True:
                A = (mask << (3 * settled_3bytes)) | settled_suffix
                self.reset(A)
                output = self.compute(break_early=True)
                if output == self._program:
                    return A
                matched_3bytes = 0
                for i in range(len(output)):
                    if output[i] == self._program[i]:
                        matched_3bytes += 1
                    else:
                        break
                if matched_3bytes > settled_3bytes + 3:
                    settled_suffix = ((mask % 8) << (3 * settled_3bytes)) | settled_suffix
                    settled_3bytes += 1
                    print(settled_3bytes)
                    break

                mask += 1






def solve_first():
    computer = Computer()
    return computer.compute()

def solve_second():
    computer = Computer()
    return computer.find_quine_smart()

def main():
    print(solve_second())


if __name__ == '__main__':
    main()
