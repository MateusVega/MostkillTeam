import json
import os

# Caminho do arquivo JSON (pasta data)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "../data", "champions.json")

# Lê o arquivo JSON
with open(JSON_PATH, "r", encoding="utf-8") as file:
    players = json.load(file)

# Calcula a média de kills por player
total_kills = sum(player["Kills"] for player in players)
media_kills = total_kills / len(players)

print(f"Média de kills por player: {media_kills:.2f}")

#Career Champions Masters
#6352.7 403 500
#70000 5000 6000