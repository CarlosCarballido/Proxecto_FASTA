class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = "ID: "+ self.identificador + " " + "Secuencia: "+self.secuencia
        return cadena
    

fastas = []
def leer_fasta(file):
    with open (file, "r") as f:
        x = []
        check = []
        for i in f:
            x.append(i.split())
        for j in range(0, len(x)):
            #print(x[j])
            for k in range(0, len(x[j])):
                #print(x[j][k])
                if x[j][k][0] == ">" and x[j+1][k][0] != ">":
                    identificador_limpio = x[j][0].split(">")
                    a = Secuencia(identificador = identificador_limpio[1],secuencia= x[j+1][0])
                    if a not in fastas:
                        fastas.append(a)
                    else:
                        for o in range(0, len(fastas)):
                            if a+o not in fastas:
                                fastas.append(a+o)
        for i in range(0, len(fastas)):
            print(fastas[i])
if __name__ == '__main__':
    leer_fasta("test_1.fasta")