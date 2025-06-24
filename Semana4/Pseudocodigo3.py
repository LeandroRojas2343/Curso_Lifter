
# Inicio

# Pedir el número al usuario
numero = int(input("Ingrese un número: "))

# Inicializar variables
suma = 0
i = 1

# Bucle mientras i <= numero
while i <= numero:
    suma = suma + i
    i = i + 1

# Mostrar resultado
print("La suma es =", suma)