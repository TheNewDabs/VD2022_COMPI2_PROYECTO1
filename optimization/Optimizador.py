from optimization.Expressions.Access import *
from optimization.Expressions.Expression import *
from optimization.Expressions.Literal import *

from optimization.Gotos.Goto import *
from optimization.Gotos.If import *

from optimization.Instructions.Assignment import *
from optimization.Instructions.CallFun import *
from optimization.Instructions.Function import *
from optimization.Instructions.Label import *
from optimization.Instructions.Print import *
from optimization.Instructions.Return import *

from optimization.Blocks import *


class Optimizador():
    reglas = []

    def __init__(self, packages, temps, code):
        self.packages = packages
        self.temps = temps
        self.code = code
        self.blocks = []

    def get_code(self):
        ret = f'package main;\n\nimport(\n\t"{self.packages}"\n);\n'
        for temp in self.temps:
            ret = ret + f'var {temp}\n'
        ret = ret + '\n'

        for func in self.code:
            ret = ret + func.get_code()+'\n\n'
        return ret

    def Mirilla(self):
        for func in self.code:
            tamano = 20
            while tamano <= len(func.instr):
                flag_opt = False
                for i in range(10):
                    aux = 0
                    while (tamano+aux) <= len(func.instr):
                        flag_opt = flag_opt or self.Regla3(
                            func.instr[0+aux:tamano+aux])
                        flag_opt = flag_opt or self.Regla6(
                            func.instr[0+aux:tamano+aux])
                        aux = aux+1

    def Bloques(self):
        self.blocks = []
        self.GenerarBloques()

    def GenerarBloques(self):
        self.GenerarLideres()
        self.CrearBloques()
        self.ConnectBloques()
        print("esperemos que jale")

    def GenerarLideres(self):
        Optimizador.reglas.append("Lideres")
        for func in self.code:
            func.instr[0].is_leader = True
            flag = False
            for instr in func.instr:
                if flag:
                    instr.is_leader = True
                    flag = False
                if type(instr) is Goto or type(instr) is If:
                    flag = True

    def CrearBloques(self):
        Optimizador.reglas.append("Creacion Bloques")
        for func in self.code:
            blocks = []
            block = None
            for instr in func.instr:
                if instr.is_leader:
                    if block is not None:
                        blocks.append(block)
                    block = Blocks(instr)
                block.code.append(instr)
            blocks.append(block)
            self.blocks.append(blocks)

    def ConnectBloques(self):
        Optimizador.reglas.append("Conexion de Bloques")
        for func in self.blocks:
            prev_block = None
            for block in func:
                if prev_block is None:
                    prev_block = block
                    continue
                prev_block.nexts.append(block)
                prev_block = block
            for block in func:
                last_ins = block.code[len(block.code)-1]
                if type(last_ins) is Goto or type(last_ins) is If:
                    label = last_ins.label
                    for check in func:
                        if type(check.first) is Label and check.first.id == label:
                            block.nexts.append(check)
                            break

    def Regla1(self, arreglo):
        Optimizador.reglas.append("Regla 1")
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]

        return ret

    def Regla2(self, arreglo):
        Optimizador.reglas.append("Regla 2")
        ret = False
        return ret

    def Regla3(self, arreglo):
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]
            if type(actual) is If and not actual.deleted:
                if i+1 < len(arreglo):
                    next_inst = arreglo[i+1]
                else:
                    return ret
                if type(next_inst) is Goto and not next_inst.deleted and i+2 < len(arreglo):
                    actual.condition.get_contrary()
                    actual.label = next_inst.label
                    next_inst.deleted = True
                    arreglo[i+2].deleted = True
                    ret = True
                    Optimizador.reglas.append("Regla 3")
        return ret

    def Regla4(self, arreglo):
        Optimizador.reglas.append("Regla 4")
        ret = False
        return ret

    def Regla5(self, arreglo):
        Optimizador.reglas.append("Regla 5")
        ret = False
        return ret

    def Regla6(self, arreglo):
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]
            if type(actual) is Assignment and not actual.deleted:
                if(actual.self_assigment()):
                    actual_opt = actual.exp.neutral_ops()
                    if actual_opt:
                        ret = True
                        actual.deleted = True
                        Optimizador.reglas.append("Regla 6")
        return ret

    def Regla7(self, arreglo):
        Optimizador.reglas.append("Regla 7")
        ret = False
        return ret

    def Regla8(self, arreglo):
        Optimizador.reglas.append("Regla 8")
        ret = False
        return ret
