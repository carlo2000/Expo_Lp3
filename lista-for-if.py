# 1.1. Listas-IF-for
# Es una colección de elementos que puede ser ordenada, modificada, etc..
# Se identifica por los corchetes
# Ejemplo:
aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#En el caso de las listas estas siempren se guardan desde la posicion 0
#aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#         0         1        2        3        4        5        6          7         8
#Hallar la posicion en la que se encuentra la alumna que deseamos
alumna = input("Que alumn@ deseamos encontrar en la lista ? ")
posicion = 0
contador=0
print("************************************************")
for alumnos in aula:
    if alumnos == alumna:
        print(f"La alumn@ {alumna} se encuentra en la posicion {posicion}")
        contador +=1
    posicion = posicion +1
if contador !=1:
    print(f"La alumn@ {alumna} no se ha encontrado en la lista")
print("************************************************")