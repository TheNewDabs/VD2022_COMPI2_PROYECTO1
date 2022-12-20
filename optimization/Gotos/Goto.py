from optimization.Instruction import *


class Goto(Instruction):

    def __init__(self, label, line, column):
        Instruction.__init__(self, line, column)
        self.label = label

    def get_code(self):
        if self.deleted:
            return ''
        return f'goto {self.label}'
