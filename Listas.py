# 1.1. Listas
# Es una colección de elementos que puede ser ordenada, modificada, etc..
# Se identifica por los corchetes
# Ejemplo:
aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#En el caso de las listas estas siempren se guardan desde la posicion 0
#aula=['Huaman', 'Pineda','Luque','Cachay','Aquino','Medina','Melendez','Higreta','Benito']
#         0         1        2        3        4        5        6          7         8
#Llamando a casa registro :
print('1. '+aula[0]) # -->Huaman
print('2. '+aula[1]) # -->Pineda
print('3. '+aula[2]) # -->Luque
print('4. '+aula[3]) # -->Cachay
print('.')
print('.')
print('.')
print('8. '+aula[7]) # -->Higreta
print('9. '+aula[8]) # -->Benito
print('TODOS :')
print(aula) 
#Observamos que si tenemos 9 registros estos se guardaran desde [0] hasta [8]
#Volviendolo general tenemos que si hay 'n' registros estos se guardaran desde [0] hasta [n-1]

#Ejemplo 2.
#Si deseamos corregir un apellido o sustituirlo por ejemplo; Benito -> Guiterrez
aula[8] = 'Guiterrez' #--> encontramos la ubicacion despues lo reemplazamos
#Mostrandolo tenemos que :
print('9. '+aula[8]) # -->Guiterrez
print('TODOS :')
print(aula) 
