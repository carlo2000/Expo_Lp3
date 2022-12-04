# 2.2 Estructuras Repetitivas
# for
# Problema 01: Ingresar un numero y enumerarlo uno por uno
cantidad = int(input("Ingresar la cantidad de numero que desea mostrar: "))
#La funcion range equivale a una lista el cual se mantendra entre 0 y "cantidad-1"
print('***********************')
for unidad in range(cantidad): 
    print(unidad+1)
print('***********************')
