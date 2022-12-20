from abstract.Instruction import *
from abstract.Return import *
from instruction.variables.Declaration import *
from expressions.Literal import *
from sym.Generator import *


class For(Instruction):
    def __init__(self, variable, value1, instructions, line, column, value2=None):
        Instruction.__init__(self, line, column)
        self.variable = variable
        self.value1 = value1
        self.value2 = value2
        self.instructions = instructions

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        left_val = self.value1.compile(env)
        if self.value2 is not None:
            right_val = self.value2.compile(env)
            temp1 = generator.add_temp()
            lit_temp1 = Literal(temp1, Type.INT, self.line, self.column)
            generator.add_expression(temp1, left_val.value, '', '')
            continue_lbl = generator.new_label()
            generator.put_label(continue_lbl)
            end_lbl = generator.new_label()
            generator.add_if(temp1, right_val.value, ">", end_lbl)
            new_env = Environment(env)
            new_env.break_lbl = end_lbl
            new_env.continue_lbl = continue_lbl
            declaration = Declaration(
                self.variable, lit_temp1, self.line, self.column)
            declaration.compile(new_env)
            generator.add_expression(temp1, temp1, '1', '+')
            self.instructions.compile(new_env)
            declaration.compile(new_env)
            generator.add_goto(continue_lbl)
            generator.put_label(end_lbl)
        else:
            if left_val.type == Type.STRING:
                move_temp = generator.add_temp()
                puntero = generator.add_temp()
                continue_lbl = generator.new_label()
                end_lbl = generator.new_label()

                generator.add_expression(puntero, left_val.value, '1', '+')
                generator.get_heap(move_temp, puntero)
                generator.put_label(continue_lbl)
                generator.add_if(move_temp, '-1', '==', end_lbl)
                new_env = Environment(env)
                new_env.break_lbl = end_lbl
                new_env.continue_lbl = continue_lbl
                generator.get_heap(move_temp, puntero)
                lit_temp1 = Literal(move_temp, Type.CHAR,
                                    self.line, self.column)
                declaration = Declaration(
                    self.variable, lit_temp1, self.line, self.column)
                declaration.compile(new_env)
                generator.add_expression(puntero, puntero, '1', '+')
                self.instructions.compile(new_env)
                generator.add_goto(continue_lbl)
                generator.put_label(end_lbl)
            elif left_val.type == Type.ARRAY:
                tipo = Type.FLOAT

                move_temp = generator.add_temp()
                puntero = generator.add_temp()
                contador = generator.add_temp()
                maximo = generator.add_temp()
                continue_lbl = generator.new_label()
                end_lbl = generator.new_label()

                generator.get_heap(maximo, left_val.value)
                generator.add_expression(puntero, left_val.value, '1', '+')
                generator.add_expression(contador, contador, '1', '+')
                generator.put_label(continue_lbl)
                generator.add_if(contador, maximo, '>', end_lbl)
                new_env = Environment(env)
                new_env.break_lbl = end_lbl
                new_env.continue_lbl = continue_lbl
                generator.get_heap(move_temp, puntero)
                lit_temp1 = Literal(move_temp, tipo, self.line, self.column)
                declaration = Declaration(
                    self.variable, lit_temp1, self.line, self.column)
                declaration.compile(new_env)
                generator.add_expression(puntero, puntero, '1', '+')
                generator.add_expression(contador, contador, '1', '+')
                self.instructions.compile(new_env)
                declaration.compile(new_env)

                generator.add_goto(continue_lbl)
                generator.put_label(end_lbl)
                print(left_val)
            else:
                print("error en la compilacion objeto no interable")
