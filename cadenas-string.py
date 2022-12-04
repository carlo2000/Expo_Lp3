#Cadenas-Strings
#Funcionalidades de la cadena y su importancia
#Ingresamos una cadena(palabra) dentro de la variable cadena
cadena=input("Ingrese Cadena: ") #Se guarda dentro de la variable
print("*************************************************")
#Llamamos funciones relacionas con cadenas que nos permiten modificarlas
mayusculas=cadena.upper() #funcion UPPER convierte a la cadena en mayusculas y lo guarda en otra variable
print(f"La cadena en mayusculas es : {mayusculas}")
minusculas=cadena.lower() #funcion Lower convierte a la cadena en minusculas y lo guarda en otra variable
print(f"La cadena en mayusculas es : {minusculas}")
listarlo = cadena.split() #funcion split convierte a la cadena en una lista y lo guarda en otra variable
print(f"La cadena convertida a lista es : {listarlo}")
#Si observamos la variable cadena que contiene nuestros datos no se ve afectada con las funciones realizadas
#Eso se da debido a que se llama a una funcion y solo lo aplica mas no modifica la variable

print("*************************************************")