# Construir una función que reciba su nombre como parámetro y que lo muestre 5 veces en la pantalla

print("-----------------------------------")
print("- MOSTRAR NOMBRE EN LA PANTALLA ---")
print("-----------------------------------")

#Definición de la función 
def mostrarNombre(nombre):
    """print(f"1. {nombre}")
    print(f"2. {nombre}")
    print(f"3. {nombre}")
    print(f"4. {nombre}")
    print(f"5. {nombre}")"""

    for i in range(1,6):
        print(f"{i} . {nombre}")


# Entrada 
nombre = input("Digite su nombre: ")

# Procesamiento
mostrarNombre(nombre)

# Salida
print("\nEso era...")
