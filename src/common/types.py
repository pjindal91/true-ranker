from typing import Dict, Set
from dataclasses import dataclass, field

@dataclass
class Player:
    name: str

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, x) -> bool:
        return self.name == x.name
    
    def toJSON(self) -> dict:
        return {"name": self.name}

@dataclass
class Match:
    # Player One
    player_1: Player
    player_1_won: int
    player_1_rank: int

    # Player Two
    player_2: Player
    player_2_won: int
    player_2_rank: int

    def __str__(self) -> str:
        return f"Player 1: {self.player_1.name}, rank: {self.player_1_rank}, won: {self.player_1_won}  v  Player 2: {self.player_2.name}, rank: {self.player_2_rank}, won: {self.player_2_won}"

    def __repr__(self) -> str:
        return f"Player 1: {self.player_1.name}, rank: {self.player_1_rank}, won: {self.player_1_won}  v  Player 2: {self.player_2.name}, rank: {self.player_2_rank}, won: {self.player_2_won}"
    
    def __hash__(self) -> int:
        return hash(f"{self.player_1.name} v {self.player_2.name}")
    
    def __eq__(self, x) -> bool:
        # 2 players can only have one match regardless of direction
        return (self.player_1 == x.player_1 and self.player_2 == x.player_2) or (self.player_1 == x.player_2 and self.player_2 == x.player_1)
    
    def toJSON(self) -> dict:
        return {
            "player_1": self.player_1.toJSON(),
            "player_1_won": self.player_1_won,
            "player_1_rank": self.player_1_rank,
            "player_2": self.player_2.toJSON(),
            "player_2_won": self.player_2_won,
            "player_2_rank": self.player_2_rank,
        }
@dataclass
class TeamInfo:
    name: str
    url: str
    players: Set[Player] = field(default_factory=set)

    def toJSON(self) -> dict:
        return {
            "name": self.name,
            "players": [player.toJSON() for player in self.players]
        }

class Matches:
    def __init__(self) -> None:
        self.all_matches: Set[Match] = set()
        self.player_to_matches: Dict[Player, Set[Match]] = {}
    
    def append(self, match: Match) -> None:
        self.all_matches.add(match) 

        # Add to player 1 map, do not add to player 2 map because it will be added when looking at team 2 report
        self.player_to_matches.setdefault(match.player_1, set()).add(match) 
    
    def to_json(self) -> Dict:
        return {
            "all_matches": self.all_matches,
            "player_to_matches": self.player_to_matches
        }