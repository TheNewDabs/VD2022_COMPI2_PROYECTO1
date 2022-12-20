from optimization.Instruction import *


class Print(Instruction):

    def __init__(self, str_to, exp, line, column):
        Instruction.__init__(self, line, column)
        self.str_to = str_to
        self.exp = exp

    def get_code(self):
        return f'fmt.Printf("{self.str_to}", int({self.exp.get_code()}));'
