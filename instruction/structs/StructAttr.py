from abstract.Instruction import *


class StructAttribute(Instruction):

    def __init__(self, id, type, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.type = type

    def compile(self, env):
        return self
