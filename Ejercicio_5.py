#Construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de los datos pares

import random

#Definir funcion

def calcular_promedio_pares(lista):
    suma = 0
    contador_pares = 0
    for i in lista:
        if i % 2 == 0:
            contador_pares += 1
            suma = suma + 1
    promedio = suma / contador_pares
    return promedio

#input
#creamos lista vacia

lista = []
#Tamaño de la lista

n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randit(1,n)
    lista.append(num)

#processing
print(f"lista: (lista)")
print(f"el promedio de la listabes {calcular_promedio_pares(lista)}")