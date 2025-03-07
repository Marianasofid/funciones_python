print("--------------------------------")
print("- BUSCAR UN NÚMERO EN CONJUNTO -")
print("--------------------------------")

#Definición de la función 
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Entrada
dato = int(input("Número a buscar: ")) #se recibe el dato del usuario

#Procesamiento
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("Lo encontré")
else:
    print("No lo encontré")

    #Salida
    print("\nEso era...")
