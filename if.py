#Condicionales.
# 2.1 Estructuras Decisivas (if, elif, else)
# if
# Problema: Dado el precio de 3 productos ingresados por el teclado, aplicar un descuento del 10% si la 
# venta es mayor o igual a 1000.
P1 = float(input("Producto 1: "))
P2 = float(input("Producto 2: "))
P3 = float(input("Producto 3: "))
total = P1 + P2 + P3
# Si el total es mayor o igual a 1000 entonces se aplica el descuento
descuento=0
if total>=1000:
    descuento= total*0.1
    print(f'El total a pagar es: {total}')
    print(f"El descuento es: {descuento}")
print(f'El importe a pagar es: {total-descuento}')
