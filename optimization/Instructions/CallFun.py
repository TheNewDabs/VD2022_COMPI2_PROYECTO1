from optimization.Instruction import *


class CallFun(Instruction):

    def __init__(self, id, line, column):
        Instruction.__init__(self, line, column)
        self.id = id

    def get_code(self):
        return f'{self.id}();'
