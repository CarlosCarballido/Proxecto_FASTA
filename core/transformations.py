from fasta import leerFasta
from sequences import Secuencia

def renombrar(listaSeq):
    nueva_lista = []
    diccionario = {}
    for seq in listaSeq:
        if seq.identificador in diccionario:
            diccionario[seq.identificador] += 1
            nuevo_id = f"{seq.identificador}.{diccionario[seq.identificador]}"
            seq.identificador = nuevo_id
            nueva_lista.append(seq)
        else:
            diccionario[seq.identificador] = 1
            nuevo_id = f"{seq.identificador}.{diccionario[seq.identificador]}"
            seq.identificador = nuevo_id
            nueva_lista.append(seq)
    return nueva_lista

def ignorarDuplicados(listaSeq):
    diccionario = {}
    for seq in listaSeq:

        if seq.identificador not in diccionario:
            diccionario[seq.identificador] = [seq]

    # Nueva lista con un objeto por seq.identificador
    nueva_lista = [listaSeq[0] for listaSeq in diccionario.values()]
    
    return nueva_lista

if __name__ == "__main__":
    listaFasta = [
        Secuencia(">S1", "ACTG"),
        Secuencia(">S1", "CCTG"),
        Secuencia(">S2", "DFGH"),
        Secuencia(">S3", "ACTG"),
        Secuencia(">S3", "PJGH"),
        Secuencia(">S4", "ADFF"),
        Secuencia(">S5", "FGHK"),
                  ]
    
    
    
    listaSinDuplicados = ignorarDuplicados(listaFasta)
    
    for i in range(0, len(listaSinDuplicados)):
        print(listaSinDuplicados[i])
    
    
    listaRenombrada = renombrar(listaFasta)
    
    for i in range(0, len(listaRenombrada)):
        print(listaRenombrada[i])
        
        