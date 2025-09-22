import requests
import json 

team = input("Enter the name of a team you'd like to get player information on:\n")
url = f'https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={team}'
response = requests.get(url)
data = response.json()

for info in data["teams"]:
    if info["strLeague"] == "NFL":
        teamID = info["idTeam"]
        teamName = info["strTeam"]
    else:
        continue

print(f'Team Name: {teamName}\nTeam ID: {teamID}')
