class Errores:
    def __init__(self, Valor, Tipo):
        self.Valor = Valor
        self.Tipo = Tipo

    def Ejecutar(self,Entorno):
        return ['','<Error>']

    def PrintError(self):
        return "\n" + self.Valor + " , " + self.Tipo

        