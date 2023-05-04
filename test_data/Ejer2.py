class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia

# Leer fichero fasta y devolver una lista de objetos secuencia donde se almacena 
# el identificador y la secuencia del archivo FASTA
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

# Imprime por consola el archivo FASTA deseado con la secuencia en una sola linea y sin añadir 
# distinciones graficas entre el identificador y la secuencia en la salida por consola
def imprimirFasta(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print(">"+f[i].identificador + "\n" + f[i].secuencia)

# Imprimir por consola el archivo fasta deseado distinguiendo entre identificador y secuencia,
# permitiendo una visualizacion mas limpia
def imprimirFastaMod(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print("ID: " + f[i].identificador + "\n" + "SECUENCIA: " + f[i].secuencia + "\n")

if __name__ == '__main__':
    
    leerFasta("test_1.fasta")
    leerFasta("test_2.fasta")
    
    imprimirFasta("test_1.fasta") 
    imprimirFasta("test_2.fasta")    
    
    imprimirFastaMod("test_1.fasta")
    imprimirFastaMod("test_2.fasta")