#Construir una funcion que reciba como parametro una lista de datos numericos y que retorne la suma de dichos datos.

import random


print("---------------------------------------")
print("----------SUMA LISTA DE DATOS----------")
print("---------------------------------------")

#Definicion de la funcion
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#Enrada 
# Creamos una lista vacia
lista = []
# Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

#Procesamiento
print("lista: ", lista)
print("la suma es : ", sumar_lista_datos(lista))

# Salida
print("\nEso era...")

    