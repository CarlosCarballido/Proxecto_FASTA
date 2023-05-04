import sys
from core.fasta import secToTXT
from CLI.argsparser import parseArgs

if __name__ == '__main__':
    #secToTXT("test_3.fasta", "datos11111.txt", "lower", 3)
     
    #Ejer5.py –-input=test_4.fasta –-output=datosEjer5.txt -–case=lower --maxLength=0
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_format.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_4.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer6.txt --case=lower --maxLength=0
    # $Env:PYTHONPATH = "C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA"

    args = parseArgs(sys.argv[1:])

    if len(args.items()) < 2:
        print("ERROR: Numero de parametros insuficiente.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
    if len(args.items()) > 4:
        print("ERROR: Numero de parametros excesivo.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
        
    if type(args["maxLength"]) != int:
        print("ERROR: El parametro --maxLength no es un entero")

    if "input" not in args:
        print("ERROR: Es necesario introducir el parametro --input")
        sys.exit(1)
    
    if "output" not in args:
        print("ERROR: Es necesario introducir el parametro --output")
        sys.exit(1)
    
    
    if "case" in args and "maxLength" in args:
        secToTXT(args["input"], args["output"], args["case"], int(args["maxLength"]))
    elif "case" in args:
        secToTXT(args["input"], args["output"], args["case"])
    elif "maxLength" in args:
        secToTXT(args["input"], args["output"], "default", int(args["maxLength"]))
    else:
        secToTXT(args["input"], args["output"])
    
    #C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_format.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer7.txt --case=lower --maxLength=0