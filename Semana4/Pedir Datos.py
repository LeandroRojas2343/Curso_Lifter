# Pedir datos al usuario
print("Ingrese su nombre:")
nombre = input()

print("Ingrese sus apellidos:")
apellidos = input()

print("Ingrese su edad:")
edad = input()

# Convertir la edad a número entero
edad = int(edad)

# Clasificar según la edad
if edad < 2:
    etapa = "bebé"
elif edad < 6:
    etapa = "niño"
elif edad < 12:
    etapa = "preadolescente"
elif edad < 18:
    etapa = "adolescente"
elif edad < 30:
    etapa = "adulto joven"
elif edad < 60:
    etapa = "adulto"
else:
    etapa = "adulto mayor"

# Mostrar el resultado
print(f"\nHola {nombre} {apellidos}, tienes {edad} años y eres un {etapa}.")

