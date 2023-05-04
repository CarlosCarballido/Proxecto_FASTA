from core.fasta import leerFasta

def renombrar(listaSeq):   
    diccionario = {}
    for objeto in listaSeq:
        contador = 1
        identificador = objeto.identificador
        if identificador in diccionario:
            diccionario[identificador].append(objeto)
            contador += 1
            print("if")
        else:
            diccionario[identificador] = [objeto.identificador + "." + str(contador)]
            print("else")
        contador = 0

    # Nueva lista con un objeto por identificador
    nueva_lista = []
    for identificador, listaSeq in diccionario.items():
        nueva_lista.append(listaSeq[0])
    
    return nueva_lista

def ignorarDuplicados(listaSeq):
        #introducir nuevo bucle que compruebe con listaSeq[seq].identificador == nuevaLista[i].identificador en la nueva lista
    diccionario = {}
    for objeto in listaSeq:
        identificador = objeto.identificador
        if identificador in diccionario:
            diccionario[identificador].append(objeto)
        else:
            diccionario[identificador] = [objeto]

    # Nueva lista con un objeto por identificador
    nueva_lista = []
    for identificador, listaSeq in diccionario.items():
        nueva_lista.append(listaSeq[0])
    
    return nueva_lista

if __name__ == "__main__":
    listaFasta = leerFasta("c:/Users/ACER/Documents/IA/Programacion_II/Proyecto/Proxecto_FASTA/test_data/test_3.fasta")
    
    listaRenombrada = renombrar(listaFasta)
    
    for i in range(0, len(listaFasta)):
        print(listaFasta[i])
        
    #listaSinDuplicados = ignorarDuplicados(listaFasta)
    
    #for i in range(0, len(listaSinDuplicados)):
    #    print(listaSinDuplicados[i])