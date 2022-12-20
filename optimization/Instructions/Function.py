from optimization.Instruction import *


class Function(Instruction):

    def __init__(self, instr, id, line, column):
        Instruction.__init__(self, line, column)
        self.instr = instr
        self.id = id

    def get_code(self):
        ret = f'func {self.id}(){{\n'
        for instruction in self.instr:
            aux_text = instruction.get_code()
            if aux_text == '':
                continue
            ret = ret + f'\t{aux_text}\n'
            if instruction.is_leader:
                ret = ret + '\t\t\t\t\t//Lider'
            ret = ret + '\n'
        ret = ret + '}'
        return ret
