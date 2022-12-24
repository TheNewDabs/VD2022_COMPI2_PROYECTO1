
class Optimizador:

    def Optimizar(self, C3DOriginal, Tipo):
        i = 0
        Estado = 0
        Cont = 0
        C3DOptimizado = ""
        while i<len(C3DOriginal):
            if C3DOriginal[i] == "/":
                if (i+1) < len(C3DOriginal) and C3DOriginal[i+1] == "*":
                    Cont = Cont + 1
                    while C3DOriginal[i] != "\n":
                        i = i + 1
                    if Estado == 0:
                        C3DOptimizado = C3DOptimizado + "/*OPTIMIZADO POR " + Tipo + "*/"
                        if (i+1) < len(C3DOriginal) and C3DOriginal[i+1] != "\n":
                            C3DOptimizado = C3DOptimizado + "\n"
                        Estado = 1
                    elif Estado == 3:
                        if Tipo == "BLOQUE":
                            C3DOptimizado = C3DOptimizado + "/*OPTIMIZADO POR " + Tipo + "*/"
                        if (i+1) < len(C3DOriginal) and C3DOriginal[i+1] != "\n":
                            C3DOptimizado = C3DOptimizado + "\n"
                        Estado = Estado + 1
                    elif Estado == 7:
                        if Tipo == "MIRILLA":
                            C3DOptimizado = C3DOptimizado + "/*OPTIMIZADO POR " + Tipo + "*/"
                        if (i+1) < len(C3DOriginal) and C3DOriginal[i+1] != "\n":
                            C3DOptimizado = C3DOptimizado + "\n"
                        Estado = Estado + 1
                    elif Estado == 10:
                        Estado = 0
                    else:
                        Estado = Estado + 1
                    i = i + 1
                else:
                    C3DOptimizado = C3DOptimizado + C3DOriginal[i]
                    i = i + 1
            else:
                C3DOptimizado = C3DOptimizado + C3DOriginal[i]
                i = i + 1
        C3DOriginal = C3DOptimizado
        C3DOptimizado = ""
        i = 0
        while i<len(C3DOriginal):
            if C3DOriginal[i] == "\n":
                C3DOptimizado = C3DOptimizado + C3DOriginal[i]
                i = i + 1
                Salida = False
                while not Salida:
                    if C3DOriginal[i] == "" or C3DOriginal[i] == "\n" or C3DOriginal[i] == "\r" or C3DOriginal[i] == "\b" or C3DOriginal[i] == "\a" or C3DOriginal[i] == " ":
                        i = i + 1
                    elif C3DOriginal[i] == "\t":
                        i = i + 1
                        Salida2 = False
                        while not Salida2:
                            if C3DOriginal[i] == "\t" or C3DOriginal[i] == " " or C3DOriginal[i] == "\n":
                                i = i + 1
                            else: 
                                Salida2 = True
                        C3DOptimizado = C3DOptimizado + '\t'            
                    else:
                        Salida = True
            C3DOptimizado = C3DOptimizado + C3DOriginal[i]
            i = i + 1
        print(Cont)
        return C3DOptimizado