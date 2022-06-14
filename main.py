import requests
import random

pokemon_id = random.choice(range(1, 152))

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
# Converts from JavaScript Object Notation into Python lists and dictionaries
pokemon_data = response.json()

print(f"You got pokemon number {pokemon_data['id']}, {pokemon_data['name'].capitalize()}!")
