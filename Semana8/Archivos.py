import json

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos["name"])       # Pikachu
print(datos["tipe"])         # ['Electric']
print(datos["level"])        # 15