from core.fasta import listaSecToTXT, leerFasta
from core.transformations import renombrar, ignorarDuplicados, invertirLista, complementearioLista

def apply_transformation(input_file, output_file, transformation):
    lista_secuencias = leerFasta(input_file)

    if transformation == "rename":
        transformed_list = renombrar(lista_secuencias)
    elif transformation == "remove":
        transformed_list = ignorarDuplicados(lista_secuencias)
    elif transformation == "invertir":
        transformed_list = invertirLista(lista_secuencias)
    elif transformation == "complementario":
        transformed_list = complementearioLista(lista_secuencias)
    else:
        print("ERROR: Transformación no válida.")
        return

    listaSecToTXT(transformed_list, output_file)