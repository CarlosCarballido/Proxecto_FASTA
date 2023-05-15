from CLI.argsparser import parseArgs
from core.script_utils import apply_transformation
import sys

if __name__ == '__main__':

    args = parseArgs(sys.argv[1:])

    if len(args.items()) < 2:
        print("Numero de parametros insuficiente.\nEs necesario introducir --input, --output y --mode")
        sys.exit(1)
    if len(args.items()) > 5:
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

    input_file = args["input"]
    output_file = args["output"]
    transformation = args["mode"]

    apply_transformation(input_file, output_file, transformation)