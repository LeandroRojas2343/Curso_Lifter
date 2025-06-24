numeros = [] 

# Pedimos 10 numeros al usuario 
for i in range(10): 
    numero = float(input(f"Ingrese el numero {i + 1}:"))
    numeros.append(numero)

    print("Numeros ingresados:", numeros)

# Numero + alto
numero_mas_alto = max(numeros)
print("El numero mas alto es:", numero_mas_alto)



