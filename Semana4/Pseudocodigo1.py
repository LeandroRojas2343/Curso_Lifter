
# Solicitar el precio al usuario
precio = float(input("Ingresar precio: "))

# Calcular el descuento según el valor del precio
if precio >= 100:
    descuento = precio * 0.10  # 10%
else:
    descuento = precio * 0.02  # 2%

# Calcular el precio final con el descuento aplicado
precio_final = precio - descuento

# Mostrar el resultado final
print("Precio original:", precio)
print("Descuento aplicado:", descuento)
print("Precio final con descuento:", precio_final)