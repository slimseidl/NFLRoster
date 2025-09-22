import requests 
import json 
import Roster

players = ["34165220", "34165066", "34164817"]  

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
        birthplace = player["strBirthLocation"]
        height = player["strHeight"]
        weight = player["strWeight"]

        print(f'{name} is a football player for the {team} of the National Football League.' 
              f' He is {height} tall and weighs {weight}.'
              f' He was born on {birth} in {birthplace}.')
    else:
        print(f'No data for {player_id}')
