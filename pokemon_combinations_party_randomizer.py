import pandas as pd
import itertools
import random


# Replace NaN values in the 'Types' column with ['Normal']
pokemon_stats['Types'].fillna('Normal', inplace=True)

# Extracting the first 151 rows from pokemon_stats
pokemon_stats_subset = pokemon_stats.head(151)

# Define a counter
combination_counter = 0

# Get a list of unique Pokémon names
unique_pokemon = pokemon_stats_subset.index.tolist()

# Loop through random combinations
for _ in range(1000):  # Adjust as needed
    random_combination = random.sample(unique_pokemon, 6)
    types_seen = set()
    types_valid = True
    
    for pokemon in random_combination:
        types = pokemon_stats_subset.loc[pokemon, 'Types']
        
        if isinstance(types, list):
            for t in types:
                if t in types_seen:
                    types_valid = False
                    break
                types_seen.add(t)
            if not types_valid:
                break
        else:  # If 'Types' is not a list (likely 'Normal' type), consider it as a single type
            if types in types_seen:
                types_valid = False
                break
            types_seen.add(types)
    
    if types_valid:
        combination_counter += 1
        print(f"Combination {combination_counter}: {random_combination}")
