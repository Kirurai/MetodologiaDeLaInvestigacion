def ordenarMayorMenor(num): #recibe un numero, devuelve el numero con las cifras ordenadas de mayor a menor

    # obtiene cada cifra del numero
    unidad = int(num) % 10
    decena = int(int(num) / 10) % 10
    centena = int(int(num) / 100) % 10
    unidadmil = int(int(num) / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]   #coloca las cifras en un vector
    menorAMayor = sorted(numeroAOrdenar)    #ordena las cifras de menor a mayor
    mayorAMenor = menorAMayor[::-1]     #invierte el orden de los valores para dejarlos de mayor a menor
    numeroOrdenado = str(mayorAMenor[0]) + str(mayorAMenor[1]) + str(mayorAMenor[2]) + str(mayorAMenor[3])  #coloca cada cifra para armar el nuevo numero

    return numeroOrdenado   #devuelve el numero ordenado de mayor a menor


def ordenarMenorMayor(num): #funcion que recibe un numero y ordena sus cifras de mayor a menor, retorna el numero ordenado

    #obtiene cada cifra del numero
    unidad = int(num) % 10
    decena = int(int(num) / 10) % 10
    centena = int(int(num) / 100) % 10
    unidadmil = int(int(num) / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]   #coloca las cifras en un vector
    menorAMayor = sorted(numeroAOrdenar)    #ordena las cifras de menor a mayor
    numeroOrdenado = str(menorAMayor[0]) + str(menorAMayor[1]) + str(menorAMayor[2]) + str(menorAMayor[3])  #coloca cada cifra para armar el nuevo numero

    return numeroOrdenado   #devuelve el numero ordenado de menor a mayor