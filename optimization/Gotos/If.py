from optimization.Instruction import *


class If(Instruction):

    def __init__(self, condition, label, line, column):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.label = label

    def get_code(self):
        return f'if ({self.condition.get_code()}) {{goto {self.label};}}'
