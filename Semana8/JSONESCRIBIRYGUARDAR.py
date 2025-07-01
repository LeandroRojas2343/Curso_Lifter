import json

nuevo_dato = {
    "name": "Charmander",
    "tipe": ["Fire"],
    "level": 10
}

with open("data.json", "w", encoding="utf-8") as archivo:
    json.dump(new_data, archivo, indent=4, ensure_ascii=False)