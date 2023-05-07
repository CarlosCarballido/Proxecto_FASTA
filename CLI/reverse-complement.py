import sys
from CLI.argsparser import parseArgs
from core.script_utils import apply_transformation
from core.fasta import listaSecToTXT, leerFasta
from core.transformations import invertirLista, complementearioLista
from argsparser import parseArgs

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
        
    
    input_file = args["input"]
    output_file = args["output"]
    mode = args["mode"]
    
    lista_secuencias = leerFasta(input_file)
    
    if mode == "invertir":
        transformed_list = invertirLista(lista_secuencias)
    elif mode == "complementario":
        transformed_list = complementearioLista(lista_secuencias)
    else:
        print("ERROR: Transformación no válida")
        sys.exit(1)
    
    listaSecToTXT(transformed_list, output_file)