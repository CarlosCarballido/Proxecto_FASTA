class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
        
    def __str__(self):
        cadena = "ID: "+ self.identificador + "\n" + "SECUENCIA: "+self.secuencia+"\n"
        return cadena
    

def leerFasta(file):
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
                        
                    crearObjetoFasta = Secuencia(identificador = identificador_limpio[1],secuencia= secuencia_limpia)

                    fastas.append(crearObjetoFasta)
    return fastas

def imprimirFasta(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print(f[i].secuencia)

def formateador(seq, case = "default", maxLenght = 0):
    x = seq
    if case == "mayuscula":
        x.secuencia = x.secuencia.upper()

    elif case == "minuscula":
        x.secuencia = x.secuencia.lower()

    if maxLenght != 0:    
        listaSeq = ""
        i = 0
        while i < len(seq.secuencia):
            j = 0
            while j < maxLenght:
                if i+j < len(seq.secuencia):
                    listaSeq += seq.secuencia[i+j]
                j += 1
            listaSeq += "\n"
            i += maxLenght
        #fastaLimpio = "\n".join([str(i) for i in listaSeq])
        return ">" + x.identificador + "\n" + listaSeq
    return ">" + x.identificador + "\n" + x.secuencia
    
        #x.secuencia = x.secuencia[0:abs(maxLenght)]
        
        #for i in range(0, len(x.secuencia)):
        #    a = x.secuencia[0:maxLenght:maxLenght]
        #fastaLimpio = "\n".join([str(i) for i in a])

def secToTXT(nombreArchivo, nombreFasta, case = "default", maxLenght = 0):
    #for i in range(0,len(leerFasta(nombreFasta))):
    #    print(leerFasta(nombreFasta)[1])
    with open(nombreArchivo, "wt") as f:
        for seq in leerFasta(nombreFasta):
            f.write(formateador(seq, case, maxLenght)+"\n")
        #f.write(formateador(leerFasta(nombreFasta),case, maxLenght))
    

if __name__ == '__main__':
    secToTXT("datos.txt", "test_4.fasta", "minuscula", 1000) # Esto tiene que sacar los caracteres de la secuencia de dos en dos