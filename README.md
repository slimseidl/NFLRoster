<h1>🏈 NFL Roster Lookup (TheSportsDB API)</h1>

This Python project provides a simple way to fetch and display NFL player information using TheSportsDB API. 

It allows you to retrieve a team’s roster (first 10 players) by a team's name.

<h2>📌 Features</h2>

Search for an NFL team by name and retrieve its team ID.

Fetch and display a team’s full roster (limited to 10 players on free tier).


<h2>🚀 Getting Started</h2>
Make sure you have:
Python 3.8+
The following libraries:
- requests
- datetime

Clone the Repo

Run an instance:

from NFL class import NFLRoster

team = NFLRoster('Bills')

team.print_info()


<h2>⚠️ Limitations<h2>
The free tier of TheSportsDB limits roster requests to 10 players per team.
To get full rosters, you need a premium key from TheSportsDB.

<h2>📜 License</h2>

Data provided by TheSportsDb (https://www.thesportsdb.com/)