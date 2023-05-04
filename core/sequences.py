
class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = self.identificador + "\n" + self.secuencia
        return cadena