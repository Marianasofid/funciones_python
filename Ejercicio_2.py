#Construir una función que reciba una cadena digitada (como parámetro) por el usuario y que lo muestre n veces en la pantalla. El valor n también es digitado por el usuario.

print("------------------------------------")
print("---- MOSTRAR CADENA N VECES EN -----")
print("-------------PANTALLA---------------")
print("------------------------------------")
#Definicion de la funcion
def mostrarCadena(cadena, n):
    for i in range(1,n+1):
        print(f"{i} . {cadena}")

#Entrada
cadena = input("Digite la cadena a mostrar: ")
n = int(input("Digite el numero de veces que quiere mostrar la cadena: "))

#Procesamiento 
mostrarCadena(cadena, n)

#Salida
print("\nEso era...")