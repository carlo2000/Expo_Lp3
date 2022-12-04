#Cadenas-Strings con For 
#Funcionalidades de la cadena y su importancia
#Ingresamos una cadena(palabra) dentro de la variable cadena
cadena=input("Ingrese Cadena: ") #Se guarda dentro de la variable
print("*************************************************")
for caracter in cadena:
    print(caracter) #Inprime letra por letra incluso los espacios vacios
print("*************************************************")
encontrar=input("Ingrese la letra a encontrar :") #creamos una variable para guardar la letra que queremos encontrar
contar = 0 #contador que nos ayudara a saber cuantas caracteres se encontraran
minuscula = cadena.lower() #funcion minuscula para poder encontrar la letra ya sea que este en mayuscula o minuscula
print("*************************************************")
for caracter in minuscula:
    if caracter == encontrar:
        contar +=1
print(f"Se encontraron {contar} letras '{encontrar}' de la cadena {cadena}")
print("*************************************************")