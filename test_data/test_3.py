class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = "ID: "+ self.identificador + " " + "Secuencia: "+self.secuencia
        return cadena
    
fastas = []
def leer_fasta(file):
    def existe_ID(a):
        for i in range(0,1):
            if a.identificador not in fastas:
                fastas.append(a)
                print("añadido")
            else:
                fastas.append(a)
                print("añadido en else")
                
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
                    existe_ID(a)
                    #for i in range(0,1):
                    #    if a.identificador not in fastas:
                    #        fastas.append(a+i)
                    #        print("añadido")
                    #    else:
                    #        fastas.append(a)
                    #        print("añadido en else")
        
        for i in range(0, len(fastas)):
            print(fastas[i])           
            
if __name__ == '__main__':
    leer_fasta("test_3.fasta")