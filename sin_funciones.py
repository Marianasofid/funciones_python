print("--------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("--------------------------------")

#Entradab
b = int(input("Número a buscar: ")) # se recibe el dato del usuario

#Procesamiento
a = [1,2,3,4,5] #Se almacena una lista de datos 
r = False #Se inicia la variable r con un valor Falso

for i in a:
    if i==b:
      print("Lo encontré")
      r = True
    if r==False:
     print ("Nn lo encontré")

#Salida

print("\nEso era...")

    