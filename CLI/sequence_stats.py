from core.sequences import Secuencia
import csv

class SequenceStatistics:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)
        self.counts = self.calculate_counts()

    def calculate_counts(self):
        counts = {
            'A': 0,
            'C': 0,
            'T': 0,
            'G': 0,
            '-': 0,
            '.': 0
        }
        for base in self.sequence:
            if base in counts:
                counts[base] += 1
        return counts


def calculate_sequence_statistics(sequence):
    return SequenceStatistics(sequence)


def calculate_sequence_list_statistics(sequence_list):
    statistics_list = [['id', 'len', 'A', 'C', 'T', 'G', '-', '.']]
    for sequence in sequence_list:
        stats = calculate_sequence_statistics(sequence.secuencia)
        sequence_stats = [sequence.identificador, stats.length, stats.counts['A'], stats.counts['C'],
                          stats.counts['T'], stats.counts['G'], stats.counts['-'], stats.counts['.']]
        statistics_list.append(sequence_stats)
    return statistics_list


def save_statistics_to_csv(statistics, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(statistics)


if __name__ == '__main__':
    import sys
    from core.fasta import leerFasta
    from argsparser import parseArgs

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
