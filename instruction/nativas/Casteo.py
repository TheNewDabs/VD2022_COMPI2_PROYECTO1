from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *

class Casteo(Instruction):
    def __init__(self,type,expresion, line, column):
        Instruction.__init__(self, line, column)
        self.type = type
        self.expresion = expresion
        self.line = line
        self.column = column

    def compile(self, env):
        val = self.expresion.compile(env)

#----------------------------------------------------------------------------FLOAT

        if self.type == 2:                                                                            
                if val.type == Type.INT:                                                           #ENTERO A DECIMAL
                    try:
                        val.value = float(val.value)
                        val.type = Type.FLOAT
                        return val                                  #SE PASA A DECIMAL CON FLOAT 
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para float.", self.line, self.column)
                elif val.type == Type.STRING:                                                         #STRING A DECIMAL   
                    try:
                        val.value = float(val.value)
                        val.type = Type.FLOAT
                        return val                                      #SE PASA A DECIMAL CON FLOAT  
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para float.", self.line, self.column)
                elif val.type == Type.CHAR:                                                         #CARACTER A DECIMAL   
                    try:
                        val.value = float(val.value)
                        val.type = Type.FLOAT
                        return val                                        #SE PASA A DECIMAL CON FLOAT  
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para float.", self.line, self.column)         
                return print("Semantico", "Tipo Erroneo de casteo para double.", self.line, self.column)


#----------------------------------------------------------------------------INT
        if self.type == 1:                                                                            
                if val.type == Type.FLOAT:                                                            #DECIMAL A ENTERO
                    try:
                        val.value = int(float(val.value))
                        val.type = Type.INT
                        return val                                         #SE PASA A DECIMAL CON FLOAT
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para int.", self.line, self.column)
                elif val.type == Type.STRING:                                                          #DECIMAL A STRING(CADENA)
                    try:
                        val.value = str(val.value)
                        val.type = Type.STRING
                        return val                                         #SE PASA A DECIMAL CON FLOAT                                        #SE PASA A CADENA CON STR  
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para int.", self.line, self.column)  
                elif val.type == Type.CHAR:                                                         #CARACTER A STRING(CADENA)
                    try:
                        val.value = ord(val.value)
                        val.type = Type.STRING
                        return val                                         #SE PASA A DECIMAL CON FLOAT                                        #SE PASA A CADENA CON STR  
                    except:
                         return print("Semantico", "NO SE PUEDE CASTEAR para int.", self.line, self.column) 
                return print("Semantico", "Tipo Erroneo de casteo para int.", self.line, self.column)   

#------------------------------------------STRING(CADENA)-----------------------------------------------------------

        if self.type == 5:                                                                            
                if val.type == Type.FLOAT:                                                           #DECIMAL A CADENA
                    try:
                        val.value = str(val.value)
                        val.type = Type.STRING
                        return val                                      #SE PASA A DECIMAL CON FLOAT
                    except:
                         return ("Semantico", "NO SE PUEDE CASTEAR para string.", self.line, self.column)
                elif val.type == Type.INT:                                                         #ENTERO A STRING(CADENA)
                    try:
                        val.value = str(val.value)
                        val.type = Type.STRING
                        return val                                        #SE PASA A CADENA CON STR  
                    except:
                         return ("Semantico", "NO SE PUEDE CASTEAR para string.", self.line, self.column)
                elif val.type == Type.ARRAY:                                                         #ARRAY A STRING(CADENA)
                    try:
                        val.value = "".join(val.value)
                        val.type = Type.STRING
                        print(val.value)
                        return val                                        #SE PASA A CADENA CON STR  
                    except:
                         return ("Semantico", "NO SE PUEDE CASTEAR para string.", self.line, self.column) 
                return ("Semantico", "Tipo Erroneo de casteo para string.", self.line, self.column)  

#------------------------------------------CARACTER(CHAR)-----------------------------------------------------------

        if self.type == 4:                                                                            
                if val.type == Type.INT:                                                           #DECIMAL A CADENA
                    try:
                        val.value = str(chr(val.value))
                        val.type = Type.STRING
                        return val                                        #SE PASA A DECIMAL CON FLOAT
                    except:
                         return ("Semantico", "NO SE PUEDE CASTEAR para char.", self.line, self.column)
                return ("Semantico", "Tipo Erroneo de casteo para CHAR.", self.line, self.column)

#------------------------------------------BOOLEANO-----------------------------------------------------------

        if self.type == 3:                                                                             
                if val.type == Type.STRING:                                                           #DECIMAL A CADENA
                    try:
                        val.value = str(val.value)
                        val.type = Type.STRING
                        return val                                       #SE PASA A DECIMAL CON FLOAT
                    except:
                         return ("Semantico", "NO SE PUEDE CASTEAR para str.", self.line, self.column)
                return ("Semantico", "Tipo Erroneo de casteo para BOOLEAN.", self.line, self.column)       