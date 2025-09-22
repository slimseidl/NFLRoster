import requests 
import json 
import Roster

players = []

for name in Roster.player_dict:
    players.append(Roster.player_dict[name]) # appending player id's from roster file to players list

# print(players)

for player_id in players:
    url = f'https://www.thesportsdb.com/api/v1/json/123/lookupplayer.php?id={player_id}'
    response = requests.get(url)
    data = response.json()
    # print(json.dumps(data,indent=2)) - Pretty prints the json data returned

    if data["players"]:
        player = data["players"][0]
        name = player["strPlayer"]
        team = player["strTeam"]
        birth = player["dateBorn"]
        birthplace = player["strBirthLocation"].replace("\n", "").replace("\t", "").strip()
        height = player["strHeight"]
        weight = player["strWeight"]
        position = player["strPosition"]
        id = player["idPlayer"]

        print(f'Player Information: {id}\n'
              f'Name: {name} | Team: {team} | Position: {position}\n'
              f'Height: {height[0:10]} | Weight: {weight[0:6]}\n'
              f'Birth Date: {birth}\nBirth Place: {birthplace}\n')
    else:
        print(f'No data for {player_id}')
