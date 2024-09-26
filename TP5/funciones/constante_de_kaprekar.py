from TP5.funciones.ordenar import *

def  rutinaKaprekar(vectorNum):  #funcion para ejecutar la rutina de Kaprekar

    CONSTANTE_KAPREKAR = 6174   #constante

    for x in vectorNum: #recorre el listado de numeros

        unidad = int(x) % 10
        decena = int(int(x) / 10) % 10
        centena = int(int(x) / 100) % 10
        unidadmil = int(int(x) / 1000)

        if x == CONSTANTE_KAPREKAR: #si el numero es igual a la constante
            print("Numero: " + str(x))  # imprime el numero
            print("Repeticiones: 0")
        elif unidad == decena == centena == unidadmil:  #si el numero es tiene por lo menos una cifra diferente
            print("Numero: " + str(x))  # imprime el numero
            print("Repeticiones: 8")
        else:   #si el numero es diferente a la constante
            repeticiones = 1    #asigna la primer repeticion
            print("Numero: "+str(x))    #imprime el numero
            numeroParaOrdenar = x   #numero a ordenar
            menor=ordenarMenorMayor(numeroParaOrdenar)  #numero ordenado de menor a mayor
            mayor=ordenarMayorMenor(numeroParaOrdenar)  #numero ordenado de mayor a menor

            while (int(mayor) - int(menor)) != CONSTANTE_KAPREKAR:  #si la resta entre el mayor y el menor es diferente a la constante, vuelve a realizar el proceso anterior
                numeroParaOrdenar = int(mayor) - int(menor)
                menor = ordenarMenorMayor(numeroParaOrdenar)
                mayor = ordenarMayorMenor(numeroParaOrdenar)
                repeticiones = repeticiones+1   #agrega una repeticion

            print("Repeticiones: "+str(repeticiones))   #imprime el numero de repeticiones necesarias para llegar a la constante


def ingresaNumeroValido(casos):   #funcion para ingresar los numeros a comprobar

    numeros=[]  #vector de numeros

    while len(numeros)<int(casos):   #mientras falten numeros

        numNuevo = input("Ingrese un numero de 4 cifras, que tenga al menos 2 diferentes: ") #pide un numero

        if len(numNuevo) == 4:  #si el numero es menor de 4 cifras

            numeros.append(numNuevo)    #se agrega el numero al vector de numeros

        else:
            print("Número erroneo. No tiene 4 cifras.")
        #fin del while


    return numeros  #regresa el vector numeros una vez lleno




