import json 

# Path to the JSON file
pokemon_file = 'pokemon.json'

# Step 1: Read existing Pokémon
try: 
    with open(pokemon_file, 'r', encoding='utf-8') as file: 
        pokemon_list = json.load(file)
except FileNotFoundError: 
    pokemon_list = []

# Step 2: Get data for the new Pokémon
print("\n--- Add New Pokémon ---")
name = input("Pokémon Name: ")
types = input("Types (separated by comma if more than one): ").split(',')

# Clean spaces
types = [t.strip() for t in types]

print("\n--- Base Stats ---")
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))

# Create dictionary for the new Pokémon
new_pokemon = {
    "name": {
        "english": name
    },
    "type": types,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}

# Step 3: Add and save to file
pokemon_list.append(new_pokemon)

with open(pokemon_file, 'w', encoding='utf-8') as file: 
    json.dump(pokemon_list, file, indent=4, ensure_ascii=False)

print(f"\n✅ Pokémon '{name}' added successfully.")




