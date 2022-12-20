from abstract.Instruction import *


class CreateStruct(Instruction):
    def __init__(self, id, attributes, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.attributes = attributes

    def compile(self, env):
        env.save_struct(self.id, self.attributes)
