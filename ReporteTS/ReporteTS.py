
class ReporteTS:
    def __init__(self, id, simbolo, ambito, fila, columna):
        self.id = id
        self.simbolo = simbolo
        self.ambito = ambito
        self.fila = fila
        self.columna = columna

    def toString(self):
        return self.id + " - " + self.simbolo + " - " + self.ambito + " [" + str(self.fila) + ", " + str(self.columna) + "]"