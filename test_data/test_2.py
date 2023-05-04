class Secuencia:
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = "ID: "+ self.identificador + "\n" + "SECUENCIA: "+self.secuencia+"\n"
        return cadena

def leer_fasta(file):
    fastas = []
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
                    
        for i in range(0, len(fastas)):
            print(fastas[i])           
            
if __name__ == '__main__':
    leer_fasta("test_2.fasta")