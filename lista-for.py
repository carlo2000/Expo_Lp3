# 1.1. Listas
# Es una colección de elementos que puede ser ordenada, modificada, etc..
# Se identifica por los corchetes
# Ejemplo:
aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#En el caso de las listas estas siempren se guardan desde la posicion 0
#aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#         0         1        2        3        4        5        6          7         8
#Llamando a casa registro :
a=1
for alumnos in aula:
    print(str(a)+'. '+alumnos)
    a=a+1

