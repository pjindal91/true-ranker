from dataclasses import dataclass, field
from typing import Dict

@dataclass
class OponentStat:
    rank: int = 0
    matches_won: int = 0
    matches_lost: int = 0
    frames_won: int = 0
    frames_lost: int = 0

    def toJSON(self) -> dict:
        return {
            "rank": self.rank,
            "matches_won": self.matches_won,
            "matches_lost": self.matches_lost,
            "frames_won": self.frames_won,
            "frames_lost": self.frames_lost,
        }

@dataclass
class PlayerStats:
    name: str
    team: str
    original_rank: int
    adjusted_rank: float
    total_frames_won: int = 0
    total_frames_lost: int = 0
    total_matches_won: int = 0
    total_matches_lost: int = 0
    oponent_breakdown: Dict[int, OponentStat] = field(default_factory=dict) # Rank to stat

    def toJSON(self) -> dict:
        return {
            "name": self.name,
            "team": self.team,
            "original_rank": self.original_rank,
            "adjusted_rank": round(self.adjusted_rank,2),
            "total_frames_won": self.total_frames_won,
            "total_frames_lost": self.total_frames_lost,
            "total_matches_won": self.total_matches_won,
            "total_matches_lost": self.total_matches_lost,
            "oponent_breakdown": {r : stat.toJSON() for r, stat in self.oponent_breakdown.items()}
        }