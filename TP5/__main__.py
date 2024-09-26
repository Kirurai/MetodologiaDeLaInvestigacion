from TP5.funciones.constante_de_kaprekar import rutinaKaprekar
from TP5.funciones.constante_de_kaprekar import ingresaNumeroValido



#main
casosDePrueba = "0"
while casosDePrueba == str(0):
    casosDePrueba = input("Ingrese el numero de casos de prueba: ") #solicita numero de caso de pruebas, no puede ser 0

numeros = ingresaNumeroValido(casosDePrueba)    #ejecuta funcion de carga de numeros

rutinaKaprekar(numeros) #ejecuta la rutina de Kaprekar