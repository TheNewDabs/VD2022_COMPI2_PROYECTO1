from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *


class If(Instruction):
    def __init__(self, condition, instructions, line, column, else_st=None):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions
        self.else_st = else_st

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_comment("iniciando el if")
        condition = self.condition.compile(env)
        if condition.type != Type.BOOL:
            print("error, condicion no booleana")
            return
        generator.put_label(condition.true_lbl)
        self.instructions.compile(env)
        if self.else_st is not None:
            exit_if = generator.new_label()
            generator.add_goto(exit_if)
        generator.put_label(condition.false_lbl)
        if self.else_st is not None:
            self.else_st.compile(env)
            generator.put_label(exit_if)
