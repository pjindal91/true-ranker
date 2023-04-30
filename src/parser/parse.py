import requests
from lxml import html
from typing import List, Set
import json
from src.common.types import TeamInfo, Match, Player
import argparse
    
COOKIES = {"T8UID": ""} # set using parsed argument
URL_PREFIX = "http://leagues2.amsterdambilliards.com"

TEAM_STANDINGS_URL = URL_PREFIX + "/8ball/abc/team_standings.php?foo=bar"
def get_team_standings() -> List[TeamInfo]:
    response = requests.get(TEAM_STANDINGS_URL, cookies=COOKIES)
    content = html.fromstring(response.content)
    hrefs = content.xpath("//td/a")
    team_infos: List[TeamInfo] = []
    for href in hrefs:
        team_infos.append(TeamInfo(href.text.strip(), href.attrib['href']))
    return team_infos

def get_team_report(team_infos: List[TeamInfo]) -> Set[Match]:
    matches: Set[Match] = set()
    for team_info in team_infos:
        response = requests.get(URL_PREFIX+team_info.url, cookies=COOKIES)
        content = html.fromstring(response.content)
        match_rows = content.xpath("//td[@class='data_level_2']/..")
        for match_row in match_rows:
            # If its a total row, then ignore
            if match_row.getchildren()[0].text_content().strip() == "TOTALS":
                continue

            player_1: Player
            player_1_won: int
            player_1_rank: int
            player_2: Player
            player_2_won: int
            player_2_rank: int

            for i, child in enumerate(match_row.getchildren()):
                text = child.text_content().strip()
                if i == 0:
                    player_1 = Player(text)
                elif i == 1:
                    player_1_rank = int(text)
                elif i == 2:
                    player_1_won = int(text)
                elif i == 3:
                    player_2 = Player(text)
                elif i == 4:
                    player_2_rank = int(text)
                elif i == 5:
                    player_2_won = int(text)
        
            matches.add(Match(player_1, player_1_won, player_1_rank, player_2, player_2_won, player_2_rank))
            team_info.players.add(player_1)

    return matches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", required=True, type=str, dest="session", metavar="s", help="session id, this is required since for any get request made by the program, it needs to set the cookie for authentication. Get your session id by first logging in to http://leagues2.amsterdambilliards.com and gettig the session id from the cookie using Inspector")
    args = parser.parse_args()
    COOKIES["T8UID"] = args.session
    team_infos = get_team_standings() # Get team infos
    matches = get_team_report(team_infos) # Get all the matches
    with open('matches.json', 'w') as file:
        json.dump([match.toJSON() for match in matches], file)
    with open('teams.json', 'w') as file:
        json.dump([team.toJSON() for team in team_infos], file)