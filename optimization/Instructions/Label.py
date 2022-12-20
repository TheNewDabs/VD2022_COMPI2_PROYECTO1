from optimization.Instruction import *


class Label(Instruction):

    def __init__(self, id, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.is_leader = True

    def get_code(self):
        if self.deleted:
            return ''
        return f'{self.id}:'
