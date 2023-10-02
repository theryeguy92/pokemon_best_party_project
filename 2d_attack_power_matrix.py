#Make it into a 2D Matrix
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/zonination/pokemon-chart/master/chart.csv", index_col=0)

# Convert the DataFrame into a 2D dictionary
attack_power_matrix = df.to_dict()

# Print the resulting 2D dictionary
print(attack_power_matrix)