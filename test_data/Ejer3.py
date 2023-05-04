class Secuencia():
    
    def __init__(self, identificador, secuencia):
        self.identificador = identificador
        self.secuencia = secuencia
    

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
        print(">"+f[i].identificador + "\n" + f[i].secuencia)

def imprimirFastaMod(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print("ID: " + f[i].identificador + "\n" + "SECUENCIA: " + f[i].secuencia + "\n")

# Devuelve una cadena a partir de la secuencia que le pasemos como primer parametro.
#
# Se le puede pasar en el segundo parametro "mayuscula" o "minuscula" para formatear
# la sequencia a mayuscula o minuscula respectivamente. Si no definimos este parametro
# tomara un valor por defecto y el formateo será la versión original; con letras mayusculas
# mezcladas con minusculas si el archivo las contiene.
#
# Se puede pasar un tercer parametro, este definirá la cantidad maxima de 
# caracteres que puede tener la cadena antes de que introduzca un salto de linea en la 
# secuencia. Si no definimos el parametro maxLenght, este tomará el valor por defecto 0;
# imprimiendo asi la cadena secuencia en una sola linea
def formateador(seq, case = "default", maxLenght = 0):
    x = seq
    if case == "mayuscula":
        x.secuencia = x.secuencia.upper()

    elif case == "minuscula":
        x.secuencia = x.secuencia.lower()

    if maxLenght != 0:    
        cadenaSeq = ""
        i = 0
        while i < len(seq.secuencia):
            j = 0
            while j < maxLenght:
                if i+j < len(seq.secuencia):
                    cadenaSeq += seq.secuencia[i+j]
                j += 1
            if i < len(seq.secuencia)-1:
                cadenaSeq += "\n"
            i += maxLenght
        return ">" + x.identificador + "\n" + cadenaSeq
    return ">" + x.identificador + "\n" + x.secuencia  
    
# Formatea e imprime un archivo FASTA.
# Se le puede pasar en el segundo parametro "mayuscula" o "minuscula" para formatear
# la sequencia a mayuscula o minuscula respectivamente. Si no definimos este parametro
# tomara un valor por defecto y el formateo será la versión original; con letras mayusculas
# mezcladas con minusculas si el archivo las contiene.
#
# Se puede pasar un tercer parametro, este definirá la cantidad maxima de 
# caracteres que puede tener la cadena antes de que introduzca un salto de linea en la 
# secuencia. Si no definimos el parametro maxLenght, este tomará el valor por defecto 0;
# imprimiendo asi la cadena secuencia en una sola linea
def imprimirFormateo(fasta, case = "default", maxLenght = 0):
    for i in leerFasta(fasta):
        print(formateador(i, case, maxLenght))

if __name__ == '__main__':
    
    formateador(leerFasta("test_3.fasta")[0], "mayuscula", 3)
    
    # Para imprimir una secuencia concreta formateada
    print(formateador(leerFasta("test_3.fasta")[0], "mayuscula", 3))
 
    imprimirFormateo("test_3.fasta", "minuscula", 3)