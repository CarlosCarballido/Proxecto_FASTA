from core.fasta import leerFasta

def renombrar(listaSeq):   

    # Introduce en el la lista "S1.0"
    for i in range(0, len(listaSeq)):
        contador = 0
        if listaSeq.count(listaSeq[i].identificador)-1 != 0:
            listaSeq[i] = listaSeq[i].identificador + "." + str(contador)
            break
        else:
            contador += 1

    return listaSeq

def ignorarDuplicados(listaSeq):
    nuevaLista = []
    
    for seq in range(0, len(listaSeq)):
        #introducir nuevo bucle que compruebe con listaSeq[seq].identificador == nuevaLista[i].identificador en la nueva lista
        if listaSeq[seq].identificador not in nuevaLista:
            nuevaLista.append(listaSeq[seq])
    
    for j in range(0, len(nuevaLista)):
        print(nuevaLista[j])
    return nuevaLista

if __name__ == "__main__":
    listaFasta = leerFasta("c:/Users/ACER/Documents/IA/Programacion_II/Proyecto/Proxecto_FASTA/test_data/test_3.fasta")
    
    #listaRenombrada = renombrar(listaFasta)
    
    for i in range(0, len(listaFasta)):
        pass
        #print(listaFasta[i])
        
    listaSinDuplicados = ignorarDuplicados(listaFasta)
    
    for i in range(0, len(listaSinDuplicados)):
        #print(listaSinDuplicados[i])
        passdd