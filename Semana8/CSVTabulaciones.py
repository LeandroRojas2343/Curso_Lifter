import csv

# Predefined list of games
games_list = [
    {
        'Name': 'Fortnite',
        'Country': 'United States',
        'Genre': 'Battle Royale',
        'Developer': 'Epic Games',
        'ESRB Rating': '(Teen)',
    },
    {
        'Name': 'Warzone',
        'Country': 'United States',
        'Genre': 'Battle Royale',
        'Developer': 'Infinity Ward',
        'ESRB Rating': 'Mature 17+',
    },
    {
        'Name': 'PUBG',
        'Country': 'South Korea',
        'Genre': 'Battle Royale',
        'Developer': 'PUBG Corporation (subsidiary of Krafton)',
        'ESRB Rating': '(Teen)',
    },
]

# Column headers
games_headers = (
    'Name',
    'Country',
    'Genre',
    'Developer',
    'ESRB Rating',
)

# Function to write a tab-separated TSV file
def write_tsv_file(file_path, data, headers):
	with open(file_path, 'w', encoding='utf-8', newline='') as file:
		writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
		writer.writeheader()
		writer.writerows(data)

# Menu to let the user add more games
def menu_add_games():
	print("Welcome to the video game registry.")
	try:
		count = int(input("How many games would you like to enter?: "))
		for i in range(count):
			print(f"\nEntering data for game #{i + 1}:")
			name = input("Game name: ")
			country = input("Country of origin: ")
			genre = input("Genre: ")
			developer = input("Developer: ")
			rating = input("ESRB Rating (e.g., Teen, Mature 17+): ")
			
			new_game = {
				'Name': name,
				'Country': country,
				'Genre': genre,
				'Developer': developer,
				'ESRB Rating': rating,
			}
			games_list.append(new_game)
	except ValueError:
		print("Please enter a valid number.")

# Run the menu
menu_add_games()

# Write to TSV file
write_tsv_file('Games_tabbed.tsv', games_list, games_headers)
print("\nFile 'Games_tabbed.tsv' saved successfully.")