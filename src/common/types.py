from __future__ import annotations 
from typing import Set
from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    rank: int

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, x) -> bool:
        return self.name == x.name
    
    def toJSON(self) -> dict:
        return {"name": self.name, "rank": self.rank}
    
    @staticmethod
    def fromJSON(d: dict) -> Player:
        return Player(d["name"], d["rank"])

@dataclass
class Match:
    # Player One
    player_1: Player
    player_1_won: int

    # Player Two
    player_2: Player
    player_2_won: int

    def __str__(self) -> str:
        return f"Player 1: {self.player_1.name, self.player_1.rank}, won: {self.player_1_won}  v  Player 2: {self.player_2.name, self.player_2.rank}, won: {self.player_2_won}"

    def __repr__(self) -> str:
        return f"Player 1: {self.player_1.name, self.player_1.rank}, won: {self.player_1_won}  v  Player 2: {self.player_2.name, self.player_2.rank}, won: {self.player_2_won}"
    
    def __hash__(self) -> int:
        # Note: This results in matches being distinct where order of player 1 and player 2 is reversed
        # Eg: P1 v P2 is different from P2 v P1
        return hash(f"{self.player_1.name} v {self.player_2.name}")
    
    def __eq__(self, x) -> bool:
        # Note: This results in matches being distinct where order of player 1 and player 2 is reversed
        # Eg: P1 v P2 is different from P2 v P1
        return self.player_1 == x.player_1 and self.player_2 == x.player_2
    
    def toJSON(self) -> dict:
        return {
            "player_1": self.player_1.toJSON(),
            "player_1_won": self.player_1_won,
            "player_2": self.player_2.toJSON(),
            "player_2_won": self.player_2_won,
        }

    @staticmethod
    def fromJSON(d: dict) -> Match:
        return Match(Player.fromJSON(d["player_1"]), d["player_1_won"], Player.fromJSON(d["player_2"]), d["player_2_won"])
    
@dataclass
class Team:
    name: str
    url: str
    players: Set[Player] = field(default_factory=set)

    def toJSON(self) -> dict:
        return {
            "name": self.name,
            "url": self.url,
            "players": [player.toJSON() for player in self.players]
        }

    @staticmethod
    def fromJSON(d: dict) -> Team:
        return Team(d["name"], d["url"], [Player.fromJSON(p) for p in d["players"]])
    