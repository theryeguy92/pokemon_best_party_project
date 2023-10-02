import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_pokemon_stats():
    page = requests.get("https://www.serebii.net/pokemon/nationalpokedex.shtml")
    soup = BeautifulSoup(page.text)
    lis = soup.find_all("td", {"class": "fooinfo", })
    df = pd.DataFrame(columns=["Name", "HP", "Att", "Def", "S.Att", "S.Def", "Spd"])
    counter = 0

    while counter < len(lis):
        df.loc[len(df.index)] = [
            lis[2 + counter].text.strip(),
            int(lis[5 + counter].text),
            int(lis[6 + counter].text),
            int(lis[7 + counter].text),
            int(lis[8 + counter].text),
            int(lis[9 + counter].text),
            int(lis[10 + counter].text)
        ]
        counter += 11

    return df.set_index("Name")

# Get the Pokemon stats DataFrame
pokemon_stats = get_pokemon_stats()

# Print the DataFrame
print(pokemon_stats)