from optimization.Expressions.Access import Access
from optimization.Instruction import *
from optimization.Expressions.Literal import *


class Assignment(Instruction):

    def __init__(self, place, exp, line, column):
        Instruction.__init__(self, line, column)
        self.place = place
        self.exp = exp

    def self_assigment(self):
        if type(self.exp) is Literal or type(self.exp) is Access:
            aux = self.place.get_code() == self.exp.get_code()
        else:
            aux = self.place.get_code() == self.exp.right.get_code(
            ) or self.place.get_code() == self.exp.left.get_code()
        return aux

    def get_code(self):
        if self.deleted:
            return ''
        return f'{self.place.get_code()} = {self.exp.get_code()}'
