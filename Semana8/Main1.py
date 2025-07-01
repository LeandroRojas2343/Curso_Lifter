# Open the input file in read mode
with open('C:/Users/Admin/Documents/Semana8/canciones.txt', 'r', encoding='utf-8') as input_file:
    songs = input_file.readlines()

# Remove leading/trailing whitespace from each line
songs = [s.strip() for s in songs]

# Sort the list alphabetically
songs.sort()

with open('C:/Users/Admin/Documents/Semana8/canciones_ordenadas.txt', 'w', encoding='utf-8') as output_file:
    for song in songs:
        output_file.write(song + '\n')

print("Songs sorted and saved successfully.")