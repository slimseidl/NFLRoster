import requests 
import json 
import TeamInfo
# Build a class out of this that calls a team and calls players from that team, then outputs the info from NFLPlayer.py

id = int(TeamInfo.teamID)

# Team Roster id = team id https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604 Philly = 134936
# Lookup Team using team id https://www.thesportsdb.com/api/v1/json/123/lookupteam.php?id=133604

roster = requests.get(f'https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id={id}')
team_data = roster.json()
# print(json.dumps(team_data,indent=2))

player_dict = {}

for players in team_data["player"]:
    name = players["strPlayer"]
    val = players["idPlayer"]
    player_dict[name] = val



# print(player_dict)
