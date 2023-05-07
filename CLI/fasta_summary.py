import sys
from argsparser import parseArgs
from sequence_stats import calculate_sequence_list_statistics, save_statistics_to_csv
from core.fasta import leerFasta

#C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_summary.py  --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer12.csv

if __name__ == '__main__':
    args = parseArgs(sys.argv[1:])

    if len(args.items()) != 2:
        print("ERROR: Número incorrecto de parámetros. Deben ser --input y --output")
        sys.exit(1)

    if "input" not in args:
        print("ERROR: Debes proporcionar el parámetro --input")
        sys.exit(1)

    if "output" not in args:
        print("ERROR: Debes proporcionar el parámetro --output")
        sys.exit(1)

    input_file = args["input"]
    output_file = args["output"]

    sequence_list = leerFasta(input_file)
    statistics = calculate_sequence_list_statistics(sequence_list)
    save_statistics_to_csv(statistics, output_file)
