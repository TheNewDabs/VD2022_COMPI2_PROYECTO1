from abstract.Instruction import *
from sym.Generator import *


class AssignAccess(Instruction):
    def __init__(self, id, access, expression, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.access = access
        self.expression = expression

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()

        val = self.expression.compile(env)
        var = env.get_var(self.id)
        temp = generator.add_temp()
        temp_pos = var.pos
        if(not var.is_global):
            temp_pos = generator.add_temp()
            generator.add_expression(temp_pos, 'P', var.pos, '+')
        generator.get_stack(temp, temp_pos)
        struct = var.struct_type
        if struct != '':
            struct = env.get_struct(struct)
            final_att = None
            final_att_pos = 0
            for att in struct:
                if att.id == self.access:
                    final_att = att
                    break
                final_att_pos = final_att_pos+1
            temp_aux = generator.add_temp()
            generator.add_expression(temp_aux, temp, final_att_pos, '+')
            generator.set_heap(temp_aux, val.value)
