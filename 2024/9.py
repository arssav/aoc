from dataclasses import dataclass

class Memory:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            encoded_blocks = map(int, f.readline().strip())
        self._memory = []
        is_file = True
        file_index = 0
        for block in encoded_blocks:
            if is_file:
                self._memory.extend([file_index] * block)
            else:
                self._memory.extend([-1] * block)
                file_index += 1
            is_file = not is_file

    def compact(self):
        end_pos = len(self._memory) - 1
        free_pos = 0
        while self._memory[free_pos] != -1:
            free_pos += 1
        while end_pos > free_pos:
            self._memory[free_pos], self._memory[end_pos] = self._memory[end_pos], self._memory[free_pos]
            while self._memory[free_pos] != -1:
                free_pos += 1
            while self._memory[end_pos] == -1:
                end_pos -= 1
    
    def checksum(self):
        i = 0
        checksum = 0
        while self._memory[i] != -1:
            checksum += i * self._memory[i]
            i += 1
        return checksum
    

@dataclass
class MemoryBlock:
    length: int
    is_file: bool
    label: int

class MemoryAdvanced:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            encoded_blocks = map(int, f.readline().strip())
        self._memory: list[MemoryBlock] = []
        is_file = True
        label = 0
        for block in encoded_blocks:
            self._memory.append(MemoryBlock(block, is_file, -1 if not is_file else label))
            if is_file:
                label += 1
            is_file = not is_file
    
    def compact(self):
        file_index = len(self._memory) - 1
        # it = 0
        while file_index > 0:
            # it += 1
            # if it > 40:
            #     break
            # print(self.memory_str())
            if not self._memory[file_index].is_file:
                file_index -= 1
                continue
            empty_block_index = 0
            while empty_block_index < file_index:
                if self._memory[empty_block_index].is_file:
                    empty_block_index += 1
                    continue
                if self._memory[empty_block_index].length < self._memory[file_index].length:
                    empty_block_index += 1
                    continue
                if self._memory[empty_block_index].length == self._memory[file_index].length:
                    self._memory[empty_block_index], self._memory[file_index] = self._memory[file_index], self._memory[empty_block_index]
                    break
                self._memory = (
                    self._memory[:empty_block_index] +
                    [self._memory[file_index], MemoryBlock(
                            self._memory[empty_block_index].length - self._memory[file_index].length,
                            False,
                            -1
                    )] +
                    self._memory[empty_block_index + 1 :file_index] +
                    [MemoryBlock(self._memory[file_index].length, False, -1)] +
                    self._memory[file_index + 1:]
                )
                file_index += 1
                break
            file_index -= 1
        
    def checksum(self):
        i = 0
        cs = 0
        for block in self._memory:
            if not block.is_file:
                i += block.length
            else:
                for j in range(block.length):
                    cs += (i + j) * block.label
                i += block.length
        return cs
    
    def memory_str(self):
        s = ''
        for block in self._memory:
            s += (str(block.label) if block.is_file else '.') * block.length
        return s
                    
                    
            

def solve_first():
    memory = Memory()
    memory.compact()
    return memory.checksum()

def solve_second():
    memory = MemoryAdvanced()
    memory.compact()
    return memory.checksum()



        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
