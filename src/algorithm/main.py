from __future__ import annotations 
import json
from src.common.types import Player, Match, Team
from typing import Dict, Set, List
from src.algorithm.types import PlayerStats, OponentStat

def read_matches(path: str) -> List[Match]:
    with open(path, 'r') as f:
        matches = json.load(f)
        return [Match.fromJSON(match) for match in matches]

def read_teams(path: str) -> List[Team]:
    with open(path, 'r') as f:
        teams = json.load(f)
        return [Team.fromJSON(team) for team in teams]

def create_graph(matches: List[Match]) -> Dict[Player, Set[Match]]:
    adjency_list: Dict[Player, Set[Match]] = {}
    for match in matches:
        adjency_list.setdefault(match.player_1, set()).add(match)
    return adjency_list

def print_graph(graph):
    for player, matches in graph.items():
        print(player)
        for match in matches:
            print(match)
        print("\n")

def adjust_ranks(graph: Dict[Player, Set[Match]], teams: List[Team]) -> List[PlayerStats]:
    players_stats: List[PlayerStats] = []
    for team in teams:
        for player in team.players:
            adjusted_rank = player.rank
            matches = graph.get(player)
            player_stats = PlayerStats(player.name, team.name, player.rank, adjusted_rank)
            for match in matches:
                # Adjust rank
                rank_difference = match.player_1.rank - match.player_2.rank
                score_difference = match.player_1_won - match.player_2_won
                player_stats.adjusted_rank += (rank_difference  + score_difference) * 0.1
                
                # Update player stats
                player_stats.total_frames_won += match.player_1_won
                player_stats.total_frames_lost += match.player_2_won
                player_stats.total_matches_won += 1 if match.player_1_won > match.player_2_won else 0
                player_stats.total_matches_lost += 1 if match.player_1_won < match.player_2_won else 0
                
                # Update player's oponent stats
                oponent_stat = player_stats.oponent_breakdown.setdefault(match.player_2.rank, OponentStat())
                oponent_stat.rank = match.player_2.rank
                oponent_stat.matches_won += 1 if match.player_1_won > match.player_2_won else 0
                oponent_stat.matches_lost += 1 if match.player_1_won < match.player_2_won else 0
                oponent_stat.frames_won += match.player_1_won
                oponent_stat.frames_lost += match.player_2_won

            players_stats.append(player_stats)
            
    return players_stats

if __name__ == '__main__':
    matches = read_matches("src/data/matches.json")
    graph = create_graph(matches)
    teams = read_teams("src/data/teams.json")
    player_stats = adjust_ranks(graph, teams)
    with open('stats.json', 'w') as file:
        json.dump([stat.toJSON() for stat in player_stats], file)
