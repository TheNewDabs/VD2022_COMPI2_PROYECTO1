from sym.Generator import *
from abstract.Instruction import *
from abstract.Return import *


class Declaration(Instruction):

    def __init__(self, id, value, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.value = value

    def compile(self, env):
        get_aux = Generator()
        generator = get_aux.get_instance()

        generator.add_comment("compilacion de valor de variable")
        val = self.value.compile(env)
        generator.add_comment("fin de compilacion de variable")
        new_var = env.save_var(
            self.id, val.type, (val.type == Type.STRING or val.type == Type.STRUCT or val.type == Type.ARRAY), val.struct_type)
        temp_pos = new_var.pos
        if(not new_var.is_global):
            temp_pos = generator.add_temp()
            generator.add_expression(temp_pos, 'P', new_var.pos, "+")
        if(val.type == Type.BOOL):
            temp_lbl = generator.new_label()
            generator.put_label(val.true_lbl)
            generator.set_stack(temp_pos, '1')
            generator.add_goto(temp_lbl)
            generator.put_label(val.false_lbl)
            generator.set_stack(temp_pos, "0")
            generator.put_label(temp_lbl)
        else:
            generator.set_stack(temp_pos, val.value)
        generator.add_space()
