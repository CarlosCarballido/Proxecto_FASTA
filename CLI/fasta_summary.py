import sys
import os
from argsparser import parseArgs
from sequence_stats import calculate_sequence_list_statistics, save_statistics_to_csv
from core.fasta import leerFasta
import matplotlib.pyplot as plt

# C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_summary.py  --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\test_data\test_3.fasta --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\core\datosEjer12.csv

if __name__ == '__main__':
    args = parseArgs(sys.argv[1:])

    if len(args.items()) != 2 and len(args.items()) != 3:
        print("ERROR: Número incorrecto de parámetros. Deben ser --input y --output")
        sys.exit(1)

    if "input" not in args:
        print("ERROR: Debes proporcionar el parámetro --input")
        sys.exit(1)

    if "output" not in args:
        print("ERROR: Debes proporcionar el parámetro --output")
        sys.exit(1)
        
    if "extra-plots-dir" in args:
        extra_plots_dir_path = args["extra-plots-dir"]

    input_path = args["input"]
    output_path = args["output"]

    if os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            if file_name.endswith(".fasta"):
                input_file = os.path.join(input_path, file_name)
                output_file = os.path.join(
                    output_path, f"{os.path.splitext(file_name)[0]}.csv")

                sequence_list = leerFasta(input_file)
                statistics = calculate_sequence_list_statistics(sequence_list)
                save_statistics_to_csv(statistics, output_file)
                
                # Generar gráfica de barras
                lengths = [len(seq.secuencia) for seq in sequence_list]

                # Generar gráfica de barras
                plt.hist(lengths, bins=10)  # Utilizar un histograma para mostrar la distribución de longitudes
                plt.xlabel('Longitud de la secuencia')
                plt.ylabel('Recuento')
                plt.title('Distribución de longitudes de las secuencias')
                plt.savefig(os.path.join(extra_plots_dir_path, f"{os.path.splitext(os.path.basename(input_file))[0]}.png"))
                plt.close()
                
    elif os.path.isfile(input_path):
        input_file = input_path
        output_file = os.path.join(
            output_path, f"{os.path.splitext(os.path.basename(input_file))[0]}.csv")

        sequence_list = leerFasta(input_file)
        statistics = calculate_sequence_list_statistics(sequence_list)
        save_statistics_to_csv(statistics, output_file)
        
       # Calcular la longitud de caracteres de cada secuencia
        lengths = [len(seq.secuencia) for seq in sequence_list]

        # Generar gráfica de barras
        plt.hist(lengths, bins=10)  # Utilizar un histograma para mostrar la distribución de longitudes
        plt.xlabel('Longitud de la secuencia')
        plt.ylabel('Recuento')
        plt.title('Distribución de longitudes de las secuencias')
        plt.savefig(os.path.join(extra_plots_dir_path, f"{os.path.splitext(file_name)[0]}.png"))
        plt.close()
        
    else:
        print("ERROR: El parámetro --input debe ser un archivo o un directorio existente")
        sys.exit(1)

# $Env:PYTHONPATH = "C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA"
# C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_summary.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\fastas --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\fastas --extra-plots-dir=
