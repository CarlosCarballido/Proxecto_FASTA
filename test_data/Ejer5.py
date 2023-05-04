import argsparser
import sys
import os

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
        
def formateador(seq, case = "default", maxLength = 0):
    x = seq
    if case == "mayuscula":
        x.secuencia = x.secuencia.upper()

    elif case == "minuscula":
        x.secuencia = x.secuencia.lower()

    if maxLength != 0:    
        cadenaSeq = ""
        i = 0
        while i < len(seq.secuencia):
            j = 0
            while j < maxLength:
                if i+j < len(seq.secuencia):
                    cadenaSeq += seq.secuencia[i+j]
                j += 1
            if i < len(seq.secuencia)-1:
                cadenaSeq += "\n"
            i += maxLength
        return ">" + x.identificador + "\n" + cadenaSeq
    return ">" + x.identificador + "\n" + x.secuencia

# Redirige la salida a un fichero de texto.
# En el primer parametro indicamos el nombre del archivo al que redirigiremos la salida.
# En el segundo parametro indicamos el nombre del archivo fasta que vamos a utilizar.
# Se le puede pasar en el tercer parametro "mayuscula" o "minuscula" para formatear
# la sequencia a mayuscula o minuscula respectivamente. Si no definimos este parametro
# tomara un valor por defecto y el formateo será la versión original; con letras mayusculas
# mezcladas con minusculas si el archivo las contiene.
#
# Se puede pasar un cuarto parametro, este definirá la cantidad maxima de 
# caracteres que puede tener la cadena antes de que introduzca un salto de linea en la 
# secuencia. Si no definimos el parametro maxLength, este tomará el valor por defecto 0;
# imprimiendo asi la cadena secuencia en una sola linea
def secToTXT(nombreFasta, nombreArchivo, case = "default", maxLength = 0):
    with open(nombreArchivo, "wt") as f:
        for seq in leerFasta(nombreFasta):
            f.write(formateador(seq, case, maxLength)+"\n")
    
if __name__ == '__main__':
    #secToTXT("test_3.fasta", "datos11111.txt", "lower", 3)
     
    #Ejer5.py –-input=test_4.fasta –-output=datosEjer5.txt -–case=lower --maxLength=0
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe Ejer5.py --input=test_4.fasta --output=datosEjer5.txt --case=lower --maxLength=0

    args = argsparser.parseArgs(sys.argv[1:])
    if args["case"] and args["maxLength"]:
        secToTXT(args["input"], args["output"], args["case"], int(args["maxLength"]))
    elif args["case"]:
        secToTXT(args["input"], args["output"], args["case"])
    elif args["maxLength"]:
        secToTXT(args["input"], args["output"], "default", int(args["maxLength"]))