from core.transformations import invertir, complementario, invertirLista, complementearioLista
from core.fasta import listaSecToTXT, leerFasta
from argsparser import parseArgs
import sys

# reverse-complement.py –-input=/path/to/input.fasta –-output=/path/to/output.fasta --mode=invertir/complementario
#C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe reverse-complement.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer10.txt --mode=invertir

if __name__ == "__main__":
    
    args = parseArgs(sys.argv[1:])
    
    if len(args.items()) < 3:
        print("ERROR: Numero de parametros insuficiente.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
    if len(args.items()) > 3:
        print("ERROR: Numero de parametros excesivo.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
        
    if args["mode"] != "invertir" and args["mode"] != "complementario":
        print("ERROR: El parametro --mode tiene que tomar los valores \"invertir\" o \"complementario\"")    
        
    if "input" not in args:
        print("ERROR: Es necesario introducir el parametro --input")
        sys.exit(1)
    
    if "output" not in args:
        print("ERROR: Es necesario introducir el parametro --output")
        sys.exit(1)
        
    
    if args["mode"] == "invertir":
        a = leerFasta(args["input"])
        for i in invertirLista(a):
            print(">" + i.identificador + "\n" + i.secuencia)
    else:
        a = leerFasta(args["input"])
        for i in complementearioLista(a):
            print(">" + i.identificador + "\n" + i.secuencia)