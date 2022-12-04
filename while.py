# 2.2 Estructuras Repetitivas
# while
# Problema 01: Ingresar un numero y enumerarlo uno por uno y lo paramos cuando lo deseemos
cantidad = int(input("Ingresar la cantidad de numero que desea mostrar: "))
para = int(input("Ingresar donde queremos pararlo: "))
#La funcion range equivale a una lista el cual se mantendra entre 0 y "cantidad-1"
print('***********************')
enumerar=1 #al enumerar comenzara desde 1
while enumerar != para:
    print(enumerar)
    enumerar=enumerar+1
print('***********************')
