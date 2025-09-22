import json 
import requests 

class NFLRoster():
    def __init__(self, team='Chiefs'):
        self.team = team


    def get_team_info(self):
        # team = input("Enter the name of a team you'd like to get player information on:\n")
        url = f'https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={self.team}'
        response = requests.get(url)
        data = response.json()

        teamID = None
        for info in data["teams"]:
            if info["strLeague"] == "NFL":
                teamID = info["idTeam"]
                break
        return teamID

        # print(f'Team Name: {teamName} Team ID: {teamID}\n')

    def get_team_name(self):
        # team = input("Enter the name of a team you'd like to get player information on:\n")
        url = f'https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={self.team}'
        response = requests.get(url)
        data = response.json()

        teamName = None
        for info in data["teams"]:
            if info["strLeague"] == "NFL":
                teamName = info["strTeam"]
                break
        return teamName
        

    def get_roster(self):
        id = self.get_team_info()

        roster = requests.get(f'https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id={id}')
        team_data = roster.json()
        # print(json.dumps(team_data,indent=2))

        player_dict = {}

        for players in team_data["player"]:
            name = players["strPlayer"]
            val = players["idPlayer"]
            player_dict[name] = val

        return player_dict

    def get_player_ID(self):
        players = []

        roster = self.get_roster()

        for name in roster:
            players.append(roster[name]) # appending player id's from roster file to players list
        return players

        # print(players)

    def print_info(self):
        
        players = self.get_player_ID()
        TeamNames = self.get_team_name()

        print(f'Roster Information for the {TeamNames}\n')


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