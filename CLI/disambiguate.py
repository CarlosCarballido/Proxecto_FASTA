import sys
from core.fasta import listaSecToTXT
from CLI.argsparser import parseArgs
import time
from core.fasta import leerFasta
from core.fasta import leerFasta
from core.sequences import Secuencia

def renombrar(listaSeq):
    nueva_lista = []
    diccionario = {}
    for seq in listaSeq:
        if seq.identificador in diccionario:
            diccionario[seq.identificador] += 1
            nuevo_id = f"{seq.identificador}.{diccionario[seq.identificador]}"
            seq.identificador = nuevo_id
            nueva_lista.append(seq)
        else:
            diccionario[seq.identificador] = 1
            nuevo_id = f"{seq.identificador}.{diccionario[seq.identificador]}"
            seq.identificador = nuevo_id
            nueva_lista.append(seq)
    return nueva_lista

def ignorarDuplicados(listaSeq):
    diccionario = {}
    for seq in listaSeq:

        if seq.identificador not in diccionario:
            diccionario[seq.identificador] = [seq]

    # Nueva lista con un objeto por seq.identificador
    nueva_lista = [listaSeq[0] for listaSeq in diccionario.values()]
    
    return nueva_lista

if __name__ == '__main__':
    #secToTXT("test_3.fasta", "datos11111.txt", "lower", 3)
     
    #Ejer5.py –-input=test_4.fasta –-output=datosEjer5.txt -–case=lower --maxLength=0
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe .\disambiguate.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer8.txt --mode=remove
    # $Env:PYTHONPATH = "C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA"
    
    args = parseArgs(sys.argv[1:])
    if "mode" in args:

        if args["mode"] == "rename":
            listaSecToTXT(renombrar(leerFasta(args["input"])), args["output"])
            
        elif args["mode"] == "remove":
            listaSecToTXT(ignorarDuplicados(leerFasta(args["input"])), args["output"])
    
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_format.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer7.txt --case=lower --maxLength=0