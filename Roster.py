import requests 
import json 
# Build a class out of this that calls a team and calls players from that team, then outputs the info from NFLPlayer.py


# Team Roster id = team id https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604 Philly = 134936
# Lookup Team using team id https://www.thesportsdb.com/api/v1/json/123/lookupteam.php?id=133604

philly = requests.get('https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=134936')
philly_data = philly.json()
# print(json.dumps(philly_data,indent=2))

name_list = ["Saquon Barkley", "A.J. Brown", "Jalen Hurts", "Will Shipley", "Cam Jurgens", "Devonta Smith", "Jalen Carter", "Cooper DeJean"]

for players in philly_data["player"]:
    if players["strPlayer"] in name_list:
        print(players["strPlayer"])
