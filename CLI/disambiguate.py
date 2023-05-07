import sys
from core.fasta import listaSecToTXT
from CLI.argsparser import parseArgs
import time
from core.fasta import leerFasta
from core.fasta import leerFasta
from core.sequences import Secuencia

if __name__ == '__main__':
    #secToTXT("test_3.fasta", "datos11111.txt", "lower", 3)
     
    #Ejer5.py –-input=test_4.fasta –-output=datosEjer5.txt -–case=lower --maxLength=0
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe .\disambiguate.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer8.txt --mode=remove
    # $Env:PYTHONPATH = "C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA"
    
    args = parseArgs(sys.argv[1:])

    if len(args.items()) < 3:
        print("Numero de parametros insuficiente.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
    if len(args.items()) > 3:
        print("Numero de parametros excesivo.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)

    if "input" not in args:
        print("Es necesario introducir el parametro --input")
        sys.exit(1)
    
    if "output" not in args:
        print("Es necesario introducir el parametro --output")
        sys.exit(1)
        
    if "mode" not in args:
        print("Es necesario introducir el parametro --mode")
        sys.exit(1)

    if args["mode"] == "rename":
        listaSecToTXT(renombrar(leerFasta(args["input"])), args["output"])
        
    elif args["mode"] == "remove":
        listaSecToTXT(ignorarDuplicados(leerFasta(args["input"])), args["output"])
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_format.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer7.txt --case=lower --maxLength=0