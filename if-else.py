#IF-ELSE
# Problema 02
# Dado el importe total de ventas realizadas por un trabajador (Ingreso por teclado,
# Categorizar que tipo de empleado es , considerando la siguiente tabla)
# Categoría: A ->[1,1000]
# Categoría: B ->[1000,2000]
# Categoría: C ->[2000,5000]
# Categoría: D ->[5000,Más]
ventas = float(input("Importe de ventas realizadas: "))
print('********************************************')
if ventas < 0:  # error porque el importe nunca es negativo
    print(f"Datos erroneos, el importe de {ventas} no puede ser negativo")
else:    
    if ventas<=1000: # se cumple si ventas es menor o  igual que 1000
        print(f"Su importe de {ventas} pertenece a la Categoría: A ->[1,1000]")
    else:
        if ventas <=2000: # se cumple si ventas es menor o  igual que 2000
            print(f"Su importe de {ventas} pertenece a la Categoría: B ->[1000,2000]")
        else:
            if ventas <= 5000: # se cumple si ventas es menor o  igual que 5000
                print(f"Su importe de {ventas} pertenece a la Categoría: C ->[2000,5000]")
            else:
                print(f"Su importe  de {ventas} pertenece a la Categoría: D ->[5000,Más]") # se cumple si ventas es mayor a 5000

print('********************************************')