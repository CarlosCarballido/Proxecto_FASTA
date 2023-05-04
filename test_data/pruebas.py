class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = "ID: "+ self.identificador + " SECUENCIA: "+self.secuencia
        return cadena
    
    #def __format__(self, case, maxLenght):

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
    return fastas           
    
def recorrerFasta(fasta, case="default", maxLenght=0):
    if case == "minuscula":
        for i in range(len(fasta)):
            #if fasta[i].__str__().lower().startswith("id"):
            fasta[i] = fasta[i].__str__().lower()
            fasta[i].replace("id:", "ID")
        print(fasta)
    elif case == "mayuscula":
        for i in range(0, len(fasta)):
            fasta[i] = fasta[i].__str__().upper()
        print(fasta)
    else:
        for i in range(0, len(fasta)):    
            print(fasta[i])
        
        
if __name__ == '__main__':
    lista1 = leer_fasta("test_1.fasta")
    lista2 = leer_fasta("test_2.fasta")
    lista3 = leer_fasta("test_3.fasta")
    lista4 = leer_fasta("test_4.fasta")
    
    recorrerFasta(lista4, "minuscula")
    #recorrerFasta(lista4, "mayuscula")
    #recorrerFasta(lista4)
    #recorrerFasta(lista2)
    #recorrerFasta(lista3)
    #recorrerFasta(lista4)