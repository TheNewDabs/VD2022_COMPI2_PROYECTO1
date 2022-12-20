from optimization.Instruction import *


class Return(Instruction):

    def __init__(self, line, column):
        Instruction.__init__(self, line, column)

    def get_code(self):
        return 'return;'
