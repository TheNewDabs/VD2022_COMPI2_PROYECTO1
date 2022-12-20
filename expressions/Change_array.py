from sym.Generator import *
from abstract.Expression import *
from abstract.Return import *


class ChangeArray(Expression):
    def __init__(self, id, indexs, value, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.indexs = indexs
        self.value = value

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        val = self.value.compile(env)
        generator.add_comment('cambiando el valor de arreglo')
        array = env.get_var(self.id)
        if array == None:
            error = {}
            error['type'] = "modificacion arreglo"
            error['text'] = "no existe el arreglo"
            Environment.errores.append(error)
            print("error no existe el arreglo")
        temp = generator.add_temp()
        temp_pos = array.pos
        if not array.is_global:
            temp_pos = generator.add_temp()
            generator.add_expression(temp_pos, 'P', array.pos, '+')
        generator.get_stack(temp, temp_pos)
        sumado_aux = generator.add_temp()
        for element in self.indexs:
            elemento = element.compile(env)
            sumado = generator.add_temp()
            length = generator.add_temp()
            generator.get_heap(length, temp)
            generator.add_expression(sumado, elemento.value, temp, '+')
            self.agregarError(length, elemento.value)
            generator.get_heap(temp, sumado)
            generator.add_expression(sumado_aux, sumado, '', '')
        generator.set_heap(sumado_aux, val.value)

    def agregarError(self, posicion, index):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        label1 = generator.new_label()
        label2 = generator.new_label()
        generator.add_if(posicion, index, '<', label1)

        # codigo se agrega aqui
        generator.add_goto(label2)
        generator.put_label(label1)
        generator.add_print('c', 105)  # i
        generator.add_print('c', 110)  # n
        generator.add_print('c', 100)  # d
        generator.add_print('c', 101)  # e
        generator.add_print('c', 120)  # x
        generator.add_print('c', 32)
        generator.add_print('c', 111)  # o
        generator.add_print('c', 117)  # u
        generator.add_print('c', 116)  # t
        generator.add_print('c', 32)
        generator.add_print('c', 111)  # o
        generator.add_print('c', 102)  # f
        generator.add_print('c', 32)
        generator.add_print('c', 114)  # r
        generator.add_print('c', 97)   # a
        generator.add_print('c', 110)  # n
        generator.add_print('c', 103)  # g
        generator.add_print('c', 101)  # e
        generator.code_in("return;")

        generator.put_label(label2)
