from optimization.Instruction import *


class Access(Instruction):
    def __init__(self, StackHeap, position, line, column):
        Instruction.__init__(self, line, column)
        self.StackHeap = StackHeap
        self.position = position

    def get_code(self):
        return f'{self.StackHeap}[int({self.position.get_code()})]'
