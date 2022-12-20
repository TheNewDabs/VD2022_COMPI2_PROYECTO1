from abstract.Expression import *
from sym.Generator import *


class AccessStruct(Expression):

    def __init__(self, id, attribute, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.attribute = attribute

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        var = env.get_var(self.id)
        temp = generator.add_temp()
        temp_pos = var.pos
        if not var.is_global:
            temp_pos = generator.add_temp()
            generator.add_expression(temp_pos, 'P', var.pos, "+")
        generator.get_stack(temp, temp_pos)
        struct = var.struct_type
        if struct != '':
            struct = env.get_struct(struct)
            final_att = None
            final_att_pos = 0
            for att in struct:
                if att.id == self.attribute:
                    final_att = att
                    break
                final_att_pos = final_att_pos+1
            temp_aux = generator.add_temp()
            ret_temp = generator.add_temp()
            generator.add_expression(temp_aux, temp, final_att_pos, '+')
            generator.get_heap(ret_temp, temp_aux)
            return Return(ret_temp, final_att.type, True)
