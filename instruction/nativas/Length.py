from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *


class Length(Instruction):
    def __init__(self, line, column, array):
        Instruction.__init__(self, line, column)
        self.array = array

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_comment("compilacion length")
        array = self.array.compile(env)
        if array is None:
            print("arreglo no existe")
            return
        temp = generator.add_temp()
        generator.add_expression(temp, array.value, '', '')
        # temp_pos = array.pos
        # generator.get_stack(temp, temp)
        generator.get_heap(temp, temp)
        return Return(temp, Type.INT, True)
