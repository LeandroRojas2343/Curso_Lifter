
print("suma de un int + un float")
y = 4 
M = 23.56
print("x + y = 27,56") #27,56

print("Suma string + string") 
Saludo = "Hola"
nombre = "Mundo"
print("nombre + saludo") # "Hola Mundo"

print("Suma de un int + string") 
texto = "Edad"
numero = "30"
print("texto + str(numero)") #Reltado: "Edad:30"

print("convertir string a int")
texto = "El numero es: "
numero = 5 
resultado = 5 
resultado = texto + str(numero)
print("resultado")

print("suma list + list")
lista1 = [1,4,5]
lista2 = [2,6,4]
print(f"""
--- Resultado de la Concatenación de Listas ---
Lista 1: {lista1} (tamaño: {len(lista1)})
Lista 2: {lista2} (tamaño: {len(lista2)})

Lista concatenada: {resultado} (tamaño total: {len(resultado)})
""") # Quise curiosiar con este print 

print("String + list")
texto = "Elementos de lista: "
lista = [2,3,6]
# lista a string 
resultado = texto + str(lista)

print("resultado")


print("float + int")
float = "2.34"
int = "4"
Resultado = int + float 
print(f"Resultado de sumar {float}+ {int} = {resultado} (tipo: {type(resultado)})")

# Suma de dos booleanos 
a = True
b = False
suma = a + b 
print("Resultado:", suma)
