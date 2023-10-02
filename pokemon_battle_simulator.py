import random
import pandas as pd
import re

# Define the attack power matrix as a 2D dictionary
df = pd.read_csv("https://raw.githubusercontent.com/zonination/pokemon-chart/master/chart.csv", index_col=0)

# Convert the DataFrame into a 2D dictionary
attack_power_matrix = df.to_dict()

# Define the function to calculate damage
def calculate_damage(attacker_Att, defender_Def, base_power, type_effectiveness):
    return (attacker_Att * base_power * type_effectiveness) / (defender_Def)

# Define the function to simulate a battle
def simulate_battle(combo, pokemon_stats_subset, attack_power_matrix):
    attacker_combo = combo[:3]
    defender_combo = combo[3:]

    attacker = random.choice(attacker_combo)
    defender = random.choice(defender_combo)

    # Remove special characters from Pokémon names
    attacker = re.sub(r'[^\x00-\x7F]+', '', attacker)
    defender = re.sub(r'[^\x00-\x7F]+', '', defender)

    print(f"Attacker: {attacker}, Defender: {defender}")  # Check the Pokémon names

    try:
        attacker_type = pokemon_stats_subset.loc[attacker, 'Types'][0]
        defender_type = pokemon_stats_subset.loc[defender, 'Types'][0]

        print(f"Attacker Type: {attacker_type}, Defender Type: {defender_type}")  # Check the types

        type_effectiveness = attack_power_matrix.get(attacker_type, {}).get(defender_type)

        print(f"Type Effectiveness: {type_effectiveness}")  # Check the type effectiveness

        if type_effectiveness is not None:
            damage = calculate_damage(attacker_Att=pokemon_stats_subset.loc[attacker, 'Att'],
                                      defender_Def=pokemon_stats_subset.loc[defender, 'Def'],
                                      base_power=pokemon_stats_subset.loc[attacker, 'Att'],  
                                      type_effectiveness=type_effectiveness)
        else:
            damage = None
    except KeyError:
        print(f"One of the Pokémon names is not in the dataset.")
        damage = None

    return attacker, defender, damage

# Assuming `random_combinations` is a list of 1000 random combinations
highest_damage = -1
winning_combination = None

for combo in random_combinations:
    attacker, defender, damage = simulate_battle(combo, pokemon_stats_subset, attack_power_matrix)
    if damage is not None and damage > highest_damage:
        highest_damage = damage
        winning_combination = combo

print(f"The winning combination is: {winning_combination} with total damage {highest_damage}")