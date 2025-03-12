#Construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de dichhos datos.

import random

print("------------------------------------")
print("-------PROMEDIO LISTA DATOS---------")
print("------------------------------------")

#Definicion de la funcion 
def calcular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + 1
    promedio = suma / len(lista)
    return promedio
#Entrada
# Creamos una lista vacia
lista = []
# Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randit(14.18)
    lista.append(num)

#Procesamiento
print("lista: ", lista)
print("El promedio de la lista es: ", calcular_promedio_lista(lista))

#SAlida
print("\nEso era...")
