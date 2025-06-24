# Inicio

# 1. Pedir los segundos al usuario
segundos = int(input("Ingresa los segundos: "))

# 2. Evaluar condiciones
if segundos == 600:
    print("Igual")
    resultado = 0  # No falta ni sobra nada
elif segundos > 600:
    print("Mayor")
    resultado = segundos - 600
    print(f"Te pasaste por {resultado} segundos de los 10 minutos.")
else:
    print("Menor")
    resultado = 600 - segundos
    print(f"Faltan {resultado} segundos para llegar a los 10 minutos.")

# Fin
 




