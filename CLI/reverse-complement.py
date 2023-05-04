from core.fasta import invertir
from core.fasta import complementario

# reverse-complement.py –-input=/path/to/input.fasta –-output=/path/to/output.fasta --mode=invertir/complementario

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
        pass
    else:
        pass