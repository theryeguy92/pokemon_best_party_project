#limit to only the first 151
import requests

def get_all_pokemon_types():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Limit to the first 151 Pokemon
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types_dict = {}
        for result in data['results']:
            name = result['name'].capitalize()
            url = result['url']
            response = requests.get(url)
            if response.status_code == 200:
                pokemon_data = response.json()
                types = [t['type']['name'].capitalize() for t in pokemon_data['types']]
                types_dict[name] = types
        return types_dict
    else:
        return None


# Get the types for all Pokémon
types_dict = get_all_pokemon_types()

# Add the types to the DataFrame
pokemon_stats['Types'] = pokemon_stats.index.map(types_dict)

# Print the updated DataFrame
print(pokemon_stats)
