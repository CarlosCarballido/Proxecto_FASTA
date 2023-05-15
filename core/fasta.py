from core.sequences import Secuencia
import sys
import queue


def leerFasta(file):
    listaIDObjetos = []
    fastas = []
    with open(file, "r") as f:
        x = []
        for i in f:
            x.append(i.split())

        for j in range(0, len(x)):
            for k in range(0, len(x[j])):
                if x[j][k][0] == ">":
                    identificador_limpio = x[j][0].split(">")
                    secuencia_completa = []

                    m = j+1

                    while x[m][0][0] != ">" and m < len(x)-1:
                        secuencia_completa.append(x[m][0])
                        m += 1

                    if m == len(x)-1:
                        secuencia_completa.append(x[-1][0])

                    secuencia_limpia = "".join(secuencia_completa)

                    listaIDObjetos.append(identificador_limpio[1])

                    fastas.append(
                        Secuencia(identificador=identificador_limpio[1], secuencia=secuencia_limpia))
    return fastas


def imprimirFasta(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print(">"+f[i].identificador + "\n" + f[i].secuencia)


def imprimirFastaMod(fasta):
    f = leerFasta(fasta)
    for i in range(0, len(f)):
        print("ID: " + f[i].identificador + "\n" +
              "SECUENCIA: " + f[i].secuencia + "\n")


def formateador(seq, case="default", maxLength=0):
    x = seq
    if case == "upper":
        x.secuencia = x.secuencia.upper()

    elif case == "lower":
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


def comprobarMaxLength(maxLength):

    if maxLength < 0:
        raise ValueError(
            "ERROR: el parametro --maxLength tiene que ser mayor o igual que 0")


def secToTXT(nombreFasta, nombreArchivo, case="default", maxLength=0):

    comprobarMaxLength(maxLength)
    with open(nombreArchivo, "wt") as f:
        for seq in leerFasta(nombreFasta):
            f.write(formateador(seq, case, maxLength)+"\n")


def listaSecToTXT(listaFasta, nombreArchivo, case="default", maxLength=0):

    comprobarMaxLength(maxLength)
    with open(nombreArchivo, "wt") as f:
        for seq in listaFasta:
            f.write(formateador(seq, case, maxLength)+"\n")
