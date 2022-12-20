from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *


class While(Instruction):

    def __init__(self, condition, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()

        continue_lbl = generator.new_label()
        generator.put_label(continue_lbl)
        condition = self.condition.compile(env)
        new_env = Environment(env)
        new_env.break_lbl = condition.false_lbl
        new_env.continue_lbl = continue_lbl
        generator.put_label(condition.true_lbl)
        self.instructions.compile(new_env)
        generator.add_goto(continue_lbl)
        generator.put_label(condition.false_lbl)
