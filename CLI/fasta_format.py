from core.fasta import secToTXT
from CLI.argsparser import parseArgs
import sys

if __name__ == '__main__':

    args = parseArgs(sys.argv[1:])

    if len(args.items()) < 2:
        print("ERROR: Numero de parametros insuficiente.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
    if len(args.items()) > 5:
        print("ERROR: Numero de parametros excesivo.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)

    if "input" not in args:
        print("ERROR: Es necesario introducir el parametro --input")
        sys.exit(1)

    if "output" not in args:
        print("ERROR: Es necesario introducir el parametro --output")
        sys.exit(1)

    if "case" in args and "maxLength" in args:
        secToTXT(args["input"], args["output"],
                 args["case"], int(args["maxLength"]))
    elif "case" in args:
        secToTXT(args["input"], args["output"], args["case"])
    elif "maxLength" in args:
        secToTXT(args["input"], args["output"],
                 "default", int(args["maxLength"]))
    else:
        secToTXT(args["input"], args["output"])
