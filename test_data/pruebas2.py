class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self, case = "default", maxLenght = 0):
        self.case = case
        if self.case == "mayuscula":
            cadena = "ID: "+ self.identificador.upper() + "\n" + "SECUENCIA: "+self.secuencia.upper()+"\n"
        elif self.case == "minuscula":
            cadena = "ID: "+ self.identificador.lower() + "\n" + "SECUENCIA: "+self.secuencia.lower()+"\n"
        else:    
            cadena = "ID: "+ self.identificador + "\n" + "SECUENCIA: "+self.secuencia+"\n"
        return cadena

fastas = []
def leer_fasta(file, case = "default", maxLenght = 0):
    with open (file, "r") as f:
        x = []
        for i in f:
            x.append(i.split())
        for j in range(0, len(x)):
            for k in range(0, len(x[j])):
                if x[j][k][0] == ">":
                    identificador_limpio = x[j][0].split(">")
                    secuencia_completa = []


                    m=j+1
                    
                    while x[m][0][0] != ">" and m < len(x)-1:
                        secuencia_completa.append(x[m][0])
                        m+=1
                    
                    if m == len(x)-1:
                        secuencia_completa.append(x[-1][0])
                        
                    secuencia_limpia = "".join(secuencia_completa)

                    a = Secuencia(identificador = identificador_limpio[1],secuencia= secuencia_limpia)
                    
                    fastas.append(a)
    return fastas
        #for i in range(0, len(fastas)):
        #    print(fastas[i])           
            
if __name__ == '__main__':
    lista1 = leer_fasta("test_1.fasta", case="mayuscula", maxLenght=0)
    lista2 = leer_fasta("test_2.fasta")
    lista3 = leer_fasta("test_3.fasta")
    lista4 = leer_fasta("test_4.fasta")
    
    print(lista1)