from core.fasta import leerFasta
from core.sequences import Secuencia
import queue
from abc import ABC, abstractmethod


class AbstractTransformer(ABC):
    @abstractmethod
    def transform(self, listaSeq):
        pass


class DuplicatedIdentifiersRemover(AbstractTransformer):
    def transform(self, listaSeq):
        return ignorarDuplicados(listaSeq)


class DuplicatedIdentifiersRenamer(AbstractTransformer):
    def transform(self, listaSeq):
        return renombrar(listaSeq)


class ReverseComplement(AbstractTransformer):
    def transform(self, listaSeq):
        #listaSeq = invertirLista(listaSeq)
        #listaSeq = complementario(listaSeq)
        return listaSeq


class SequenceListTransformer:
    def __init__(self, transformations):
        self.transformations = transformations

    def apply_transformations(self, listaSeq):
        transformed_listaSeq = listaSeq
        for transformation in self.transformations:
            transformed_listaSeq = transformation.transform(transformed_listaSeq)
        return transformed_listaSeq

def renombrar(listaSeq):
    nueva_lista = []
    diccionario = {}
    for seq in listaSeq:
        if seq.identificador in diccionario:
            diccionario[seq.identificador] += 1
            seq.identificador = f"{seq.identificador}.{diccionario[seq.identificador]}"
            nueva_lista.append(seq)
        else:
            diccionario[seq.identificador] = 1
            seq.identificador = f"{seq.identificador}.{diccionario[seq.identificador]}"
            nueva_lista.append(seq)
    return nueva_lista


def ignorarDuplicados(listaSeq):
    diccionario = {}
    for seq in listaSeq:

        if seq.identificador not in diccionario:
            diccionario[seq.identificador] = [seq]

    nueva_lista = [listaSeq[0] for listaSeq in diccionario.values()]

    return nueva_lista


def invertir(seq):
    q = queue.Queue()

    for i in range(0, len(seq.secuencia)):
        q.put(seq.secuencia[i])

    secuencia_invertida = ""

    while not q.empty():
        secuencia_invertida = str(q.get()) + secuencia_invertida

    return secuencia_invertida


def invertirLista(listaSeq):
    listaNueva = []
    for i in listaSeq:
        i.secuencia = invertir(i)
        listaNueva.append(i)
    return listaNueva


def complementario(seq):
    complementos = {"A": "T", "T": "A", "C": "G", "G": "C"}

    # Iteramos sobre cada letra de la cadena y la reemplazamos con su complementaria
    ayudanteComplementario = ""
    for letra in seq.secuencia:
        if letra in complementos.keys():
            ayudanteComplementario += complementos[letra]

    seq.secuencia = ayudanteComplementario

    # Devolvemos la cadena complementaria invertida
    return seq.secuencia


def complementearioLista(listaSeq):
    listaNueva = []
    for i in listaSeq:
        i.secuencia = complementario(i)
        listaNueva.append(i)
    return listaNueva


if __name__ == "__main__":

    """
        Codigo Apartado 8
    """
    # listaFasta = [
    #    Secuencia(">S1", "ACTG"),
    #    Secuencia(">S1", "CCTG"),
    #    Secuencia(">S2", "DFGH"),
    #    Secuencia(">S3", "ACTG"),
    #    Secuencia(">S3", "PJGH"),
    #    Secuencia(">S4", "ADFF"),
    #    Secuencia(">S5", "FGHK"),
    #              ]
    #
    #
    #
    # print("\nLista sin duplicados:\n")
    # listaSinDuplicados = ignorarDuplicados(listaFasta)
    #
    # for i in range(0, len(listaSinDuplicados)):
    #    print(listaSinDuplicados[i])
    #
    # print("\n\n\nLista Renombrada:\n")
    # listaRenombrada = renombrar(listaFasta)
    #
    # for i in range(0, len(listaRenombrada)):
    #    print(listaRenombrada[i])
    #

    """
    Codigo Apartado 10
    """
    listaFasta = [
        Secuencia(">S1", "ACTG"),
        Secuencia(">S1", "CCTG"),
        Secuencia(">S2", "DFGH"),
        Secuencia(">S3", "ACTG"),
        Secuencia(">S3", "PJGH"),
        Secuencia(">S4", "ADFF"),
        Secuencia(">S5", "FGHK"),
    ]

    transformer = SequenceListTransformer([
        DuplicatedIdentifiersRemover(),
        DuplicatedIdentifiersRenamer(),
        ReverseComplement()
    ])

    transformed_listaSeq = transformer.apply_transformations(listaFasta)

    # Imprimir las secuencias transformadas
    for sequence in transformed_listaSeq:
        print(sequence)

# $Env:PYTHONPATH = "C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA"
# C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe fasta_summary.py --input=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\fastas --output=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\fastas --extra-plots-dir=C:\Users\ACER\Documents\IA\Programacion_II\Proyecto\Proxecto_FASTA\fastas
