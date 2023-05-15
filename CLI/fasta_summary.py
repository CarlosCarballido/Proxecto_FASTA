from argsparser import parseArgs
from sequence_stats import calculate_sequence_list_statistics, save_statistics_to_csv, SequenceStatistics
from core.fasta import leerFasta
import matplotlib.pyplot as plt
import sys
import os

def imprimirBarras(lengths,extra_plots_dir_path,input_file):
    plt.hist(lengths, bins=10)
    plt.xlabel('Longitud de la secuencia')
    plt.ylabel('Recuento')
    plt.title('Distribución de longitudes de las secuencias')
    plt.savefig(os.path.join(extra_plots_dir_path, f"{os.path.splitext(os.path.basename(input_file))[0]}GraficoBarras.png"))
    plt.close()


def imprimirBoxPlot(lengths,extra_plots_dir_path,file_name):
    plt.boxplot(lengths)
    plt.xticks(range(1, 5), ['A', 'C', 'T', 'G'])
    plt.xlabel('Base')
    plt.ylabel('Longitud de la secuencia')
    plt.savefig(os.path.join(extra_plots_dir_path,f"{os.path.splitext(file_name)[0]}BoxPlot.png"))
    plt.close()

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
                output_file = os.path.join(output_path, f"{os.path.splitext(file_name)[0]}.csv")

                sequence_list = leerFasta(input_file)
                statistics = calculate_sequence_list_statistics(sequence_list)
                save_statistics_to_csv(statistics, output_file)

                lengths = [len(seq.secuencia) for seq in sequence_list]

                imprimirBarras(lengths,extra_plots_dir_path,input_file)
                
                lengths_A = [seq.secuencia.count('A')/len(seq.secuencia) for seq in sequence_list]
                lengths_C = [seq.secuencia.count('C')/len(seq.secuencia) for seq in sequence_list]
                lengths_T = [seq.secuencia.count('T')/len(seq.secuencia) for seq in sequence_list]
                lengths_G = [seq.secuencia.count('G')/len(seq.secuencia) for seq in sequence_list]
                
                lengths = [lengths_A, lengths_C, lengths_T, lengths_G]
                
                imprimirBoxPlot(lengths,extra_plots_dir_path,input_file)
                


    elif os.path.isfile(input_path):
        input_file = input_path
        output_file = os.path.join(output_path, f"{os.path.splitext(os.path.basename(input_file))[0]}.csv")

        sequence_list = leerFasta(input_file)
        statistics = calculate_sequence_list_statistics(sequence_list)
        save_statistics_to_csv(statistics, output_file)

        lengths = [len(seq.secuencia) for seq in sequence_list]

        imprimirBarras(lengths,extra_plots_dir_path,input_file)
        
        lengths_A = [seq.secuencia.count('A')/len(seq.secuencia) for seq in sequence_list]
        lengths_C = [seq.secuencia.count('C')/len(seq.secuencia) for seq in sequence_list]
        lengths_T = [seq.secuencia.count('T')/len(seq.secuencia) for seq in sequence_list]
        lengths_G = [seq.secuencia.count('G')/len(seq.secuencia) for seq in sequence_list]

        lengths = [lengths_A, lengths_C, lengths_T, lengths_G]

        imprimirBoxPlot(lengths,extra_plots_dir_path,input_file)


    else:
        print("ERROR: El parámetro --input debe ser un archivo o un directorio existente")
        sys.exit(1)