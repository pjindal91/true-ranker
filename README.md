# True Ranker

True ranking algorithm for Amsterdam Eight ball league. It retrieves data from the eight ball league website and based on the matches and its results, adjusts the player rankings.

# Setup

For setting up development, simply run the following commands to create virtual environment and setup dependencies.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Parsing

For getting and parsing the data from amsterdam eight ball league, use the parser provided in `src/parser`. It can be invoked from the root directory as follows:

```
python3 -m src.parser.parse --session <id>
```

To successfully authenticate the http get request, the program needs to set the cookie with session id. This session id should be provided in the argument while invoking the program. The session id can be found by logging in to http://leagues2.amsterdambilliards.com/ and getting the cooking _T8UID_ value from the browser Inspector. This is required to be a valid(non-expired) session id else the program would not output valid data.

It would create two output files namely `matches.json` and `teams.json`.

- `matches.json` contains the details of all the matches in the season.
- `teams.json` contains the details of all the teams.

These files are created by retreiving the data from eight ball league website and parsing it. The example data is provided in `src/parser/example_html`.

# Algorithm

Algorithm to adjust the ranks can be invoked by following command:

```
python3 -m src.algorithm.main
```

The algorithm assumes there is data of matches and teams in the `src/data` folder in files `teams.json` and `matches.json`. These two files are created by the above parsing step.

The algorithm adjusts the rank of the players based on the following:

```
rank_difference = player_rank - opponent_rank
score_difference = frames_player_won - frames_opponent_won
adjusted = rank + (rank_difference + score_difference) * 0.1
```

The rank is adjusted repeatedly for every single match result.

Finally the statistics with adjusted rank is written out in file `stats.json`.

# Results

## Segfault Team

```
{
        "name": "Shiyi Li",
        "team": "Segfault",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 22,
        "total_frames_lost": 22,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Piyush Jindal",
        "team": "Segfault",
        "original_rank": 6,
        "adjusted_rank": 5.4,
        "total_frames_won": 33,
        "total_frames_lost": 47,
        "total_matches_won": 2,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 14,
                "frames_lost": 28
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Tyler King",
        "team": "Segfault",
        "original_rank": 3,
        "adjusted_rank": 2.5,
        "total_frames_won": 2,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Kiran Gavali",
        "team": "Segfault",
        "original_rank": 6,
        "adjusted_rank": 6.0,
        "total_frames_won": 28,
        "total_frames_lost": 33,
        "total_matches_won": 2,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Saurabh Baisane",
        "team": "Segfault",
        "original_rank": 5,
        "adjusted_rank": 6.3,
        "total_frames_won": 51,
        "total_frames_lost": 29,
        "total_matches_won": 9,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 0,
                "frames_won": 23,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Shashidhar Sundareisan",
        "team": "Segfault",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 48,
        "total_frames_lost": 44,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 17,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Stan Liu",
        "team": "Segfault",
        "original_rank": 4,
        "adjusted_rank": 5.1,
        "total_frames_won": 48,
        "total_frames_lost": 29,
        "total_matches_won": 9,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            }
        }
    }
```

## Doom Team

```
{
        "name": "Donnell Griffith",
        "team": "Doom",
        "original_rank": 7,
        "adjusted_rank": 6.6,
        "total_frames_won": 22,
        "total_frames_lost": 32,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 18
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Brad Fels",
        "team": "Doom",
        "original_rank": 7,
        "adjusted_rank": 9.5,
        "total_frames_won": 44,
        "total_frames_lost": 28,
        "total_matches_won": 6,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Daniel Rapp",
        "team": "Doom",
        "original_rank": 5,
        "adjusted_rank": 7.1,
        "total_frames_won": 66,
        "total_frames_lost": 43,
        "total_matches_won": 10,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 3,
                "frames_won": 32,
                "frames_lost": 25
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 20,
                "frames_lost": 11
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Kevin Chen",
        "team": "Doom",
        "original_rank": 8,
        "adjusted_rank": 11.2,
        "total_frames_won": 28,
        "total_frames_lost": 20,
        "total_matches_won": 4,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 13
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Bea Minor",
        "team": "Doom",
        "original_rank": 5,
        "adjusted_rank": 4.9,
        "total_frames_won": 28,
        "total_frames_lost": 29,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 14
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Michael Jones",
        "team": "Doom",
        "original_rank": 4,
        "adjusted_rank": 2.7,
        "total_frames_won": 30,
        "total_frames_lost": 41,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 16,
                "frames_lost": 20
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Beth Joy",
        "team": "Doom",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 22,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    }
```

## All Players

```
[
    {
        "name": "Malhar Desai",
        "team": "Avenue Cue",
        "original_rank": 6,
        "adjusted_rank": 8.9,
        "total_frames_won": 59,
        "total_frames_lost": 36,
        "total_matches_won": 9,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "Kunick Kapadia",
        "team": "Avenue Cue",
        "original_rank": 6,
        "adjusted_rank": 7.4,
        "total_frames_won": 41,
        "total_frames_lost": 27,
        "total_matches_won": 6,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 15
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Ana Verma",
        "team": "Avenue Cue",
        "original_rank": 4,
        "adjusted_rank": 3.0,
        "total_frames_won": 34,
        "total_frames_lost": 34,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Abhi Chopra",
        "team": "Avenue Cue",
        "original_rank": 4,
        "adjusted_rank": 4.4,
        "total_frames_won": 26,
        "total_frames_lost": 20,
        "total_matches_won": 5,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 15,
                "frames_lost": 7
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Rahul Kakar",
        "team": "Avenue Cue",
        "original_rank": 5,
        "adjusted_rank": 8.3,
        "total_frames_won": 53,
        "total_frames_lost": 27,
        "total_matches_won": 9,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 4,
                "matches_lost": 0,
                "frames_won": 19,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 2
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 12,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Neelam Kapadia",
        "team": "Avenue Cue",
        "original_rank": 6,
        "adjusted_rank": 5.2,
        "total_frames_won": 32,
        "total_frames_lost": 42,
        "total_matches_won": 2,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 6,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Maria Pederson",
        "team": "Cue Tang Clan",
        "original_rank": 3,
        "adjusted_rank": 2.1,
        "total_frames_won": 26,
        "total_frames_lost": 25,
        "total_matches_won": 6,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Ben Moe",
        "team": "Cue Tang Clan",
        "original_rank": 5,
        "adjusted_rank": 5.3,
        "total_frames_won": 15,
        "total_frames_lost": 13,
        "total_matches_won": 2,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Troy Holden",
        "team": "Cue Tang Clan",
        "original_rank": 5,
        "adjusted_rank": 4.6,
        "total_frames_won": 38,
        "total_frames_lost": 35,
        "total_matches_won": 6,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 4,
                "matches_lost": 0,
                "frames_won": 25,
                "frames_lost": 16
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "Aiss Guerfi",
        "team": "Cue Tang Clan",
        "original_rank": 5,
        "adjusted_rank": 4.2,
        "total_frames_won": 12,
        "total_frames_lost": 20,
        "total_matches_won": 1,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Rudi Hanja",
        "team": "Cue Tang Clan",
        "original_rank": 5,
        "adjusted_rank": 6.5,
        "total_frames_won": 65,
        "total_frames_lost": 46,
        "total_matches_won": 11,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 4,
                "matches_lost": 0,
                "frames_won": 23,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 2,
                "frames_won": 21,
                "frames_lost": 18
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Perrie Grace",
        "team": "Cue Tang Clan",
        "original_rank": 3,
        "adjusted_rank": 2.3,
        "total_frames_won": 5,
        "total_frames_lost": 9,
        "total_matches_won": 0,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Sean Donovan",
        "team": "Cue Tang Clan",
        "original_rank": 6,
        "adjusted_rank": 7.0,
        "total_frames_won": 31,
        "total_frames_lost": 24,
        "total_matches_won": 5,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Reese Pozgay",
        "team": "Cue Tang Clan",
        "original_rank": 4,
        "adjusted_rank": 4.9,
        "total_frames_won": 34,
        "total_frames_lost": 24,
        "total_matches_won": 6,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Shreyans Sheth",
        "team": "Chalk Is Cheap",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 27,
        "total_frames_lost": 30,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 11
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Ariel Salazar",
        "team": "Chalk Is Cheap",
        "original_rank": 4,
        "adjusted_rank": 3.2,
        "total_frames_won": 17,
        "total_frames_lost": 20,
        "total_matches_won": 3,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Evan Young",
        "team": "Chalk Is Cheap",
        "original_rank": 5,
        "adjusted_rank": 5.2,
        "total_frames_won": 30,
        "total_frames_lost": 23,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 19,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Lutz Jacob (Forfeit)",
        "team": "Chalk Is Cheap",
        "original_rank": 4,
        "adjusted_rank": 4.5,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Lutz Jacob",
        "team": "Chalk Is Cheap",
        "original_rank": 5,
        "adjusted_rank": 5.4,
        "total_frames_won": 42,
        "total_frames_lost": 27,
        "total_matches_won": 7,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 10
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Evan Young (Forfeit)",
        "team": "Chalk Is Cheap",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Mike Daley",
        "team": "Chalk Is Cheap",
        "original_rank": 3,
        "adjusted_rank": 1.7,
        "total_frames_won": 21,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Shreyans Sheth (Forfeit)",
        "team": "Chalk Is Cheap",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Alex Basile",
        "team": "Chalk Is Cheap",
        "original_rank": 3,
        "adjusted_rank": 3.3,
        "total_frames_won": 24,
        "total_frames_lost": 15,
        "total_matches_won": 4,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Lakshmi Babureddy",
        "team": "Chalk Is Cheap",
        "original_rank": 3,
        "adjusted_rank": 2.1,
        "total_frames_won": 22,
        "total_frames_lost": 21,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Alex Borovik",
        "team": "Chalk Is Cheap",
        "original_rank": 7,
        "adjusted_rank": 7.3,
        "total_frames_won": 36,
        "total_frames_lost": 35,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 12
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Alex Basile (Forfeit)",
        "team": "Chalk Is Cheap",
        "original_rank": 3,
        "adjusted_rank": 3.4,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Donnell Griffith",
        "team": "Doom",
        "original_rank": 7,
        "adjusted_rank": 6.6,
        "total_frames_won": 22,
        "total_frames_lost": 32,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 18
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Brad Fels",
        "team": "Doom",
        "original_rank": 7,
        "adjusted_rank": 9.5,
        "total_frames_won": 44,
        "total_frames_lost": 28,
        "total_matches_won": 6,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Daniel Rapp",
        "team": "Doom",
        "original_rank": 5,
        "adjusted_rank": 7.1,
        "total_frames_won": 66,
        "total_frames_lost": 43,
        "total_matches_won": 10,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 3,
                "frames_won": 32,
                "frames_lost": 25
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 20,
                "frames_lost": 11
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Kevin Chen",
        "team": "Doom",
        "original_rank": 8,
        "adjusted_rank": 11.2,
        "total_frames_won": 28,
        "total_frames_lost": 20,
        "total_matches_won": 4,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 13
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Bea Minor",
        "team": "Doom",
        "original_rank": 5,
        "adjusted_rank": 4.9,
        "total_frames_won": 28,
        "total_frames_lost": 29,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 14
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Michael Jones",
        "team": "Doom",
        "original_rank": 4,
        "adjusted_rank": 2.7,
        "total_frames_won": 30,
        "total_frames_lost": 41,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 16,
                "frames_lost": 20
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Beth Joy",
        "team": "Doom",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 22,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Hebe Joy",
        "team": "The Chalking Dead",
        "original_rank": 5,
        "adjusted_rank": 5.2,
        "total_frames_won": 35,
        "total_frames_lost": 40,
        "total_matches_won": 3,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 15,
                "frames_lost": 14
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            }
        }
    },
    {
        "name": "Kevin Li",
        "team": "The Chalking Dead",
        "original_rank": 8,
        "adjusted_rank": 8.3,
        "total_frames_won": 16,
        "total_frames_lost": 24,
        "total_matches_won": 0,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 13
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Yao Bao",
        "team": "The Chalking Dead",
        "original_rank": 6,
        "adjusted_rank": 7.1,
        "total_frames_won": 49,
        "total_frames_lost": 48,
        "total_matches_won": 7,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 8
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ken Yu",
        "team": "The Chalking Dead",
        "original_rank": 6,
        "adjusted_rank": 6.4,
        "total_frames_won": 14,
        "total_frames_lost": 14,
        "total_matches_won": 2,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Jonathan Tao",
        "team": "The Chalking Dead",
        "original_rank": 6,
        "adjusted_rank": 7.7,
        "total_frames_won": 57,
        "total_frames_lost": 48,
        "total_matches_won": 8,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 8
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "David Yang",
        "team": "The Chalking Dead",
        "original_rank": 5,
        "adjusted_rank": 4.3,
        "total_frames_won": 35,
        "total_frames_lost": 40,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 14
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Michael Chen",
        "team": "The Chalking Dead",
        "original_rank": 5,
        "adjusted_rank": 5.5,
        "total_frames_won": 27,
        "total_frames_lost": 22,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Shiyi Li",
        "team": "Segfault",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 22,
        "total_frames_lost": 22,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Piyush Jindal",
        "team": "Segfault",
        "original_rank": 6,
        "adjusted_rank": 5.4,
        "total_frames_won": 33,
        "total_frames_lost": 47,
        "total_matches_won": 2,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 14,
                "frames_lost": 28
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Tyler King",
        "team": "Segfault",
        "original_rank": 3,
        "adjusted_rank": 2.5,
        "total_frames_won": 2,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Kiran Gavali",
        "team": "Segfault",
        "original_rank": 6,
        "adjusted_rank": 6.0,
        "total_frames_won": 28,
        "total_frames_lost": 33,
        "total_matches_won": 2,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Saurabh Baisane",
        "team": "Segfault",
        "original_rank": 5,
        "adjusted_rank": 6.3,
        "total_frames_won": 51,
        "total_frames_lost": 29,
        "total_matches_won": 9,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 0,
                "frames_won": 23,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Shashidhar Sundareisan",
        "team": "Segfault",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 48,
        "total_frames_lost": 44,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 17,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Stan Liu",
        "team": "Segfault",
        "original_rank": 4,
        "adjusted_rank": 5.1,
        "total_frames_won": 48,
        "total_frames_lost": 29,
        "total_matches_won": 9,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Dag Dereje",
        "team": "Shotskis",
        "original_rank": 4,
        "adjusted_rank": 3.2,
        "total_frames_won": 26,
        "total_frames_lost": 26,
        "total_matches_won": 4,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 17,
                "frames_lost": 17
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Taylor Crossland (Forfeit)",
        "team": "Shotskis",
        "original_rank": 4,
        "adjusted_rank": 4.5,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Jacob Shomstein",
        "team": "Shotskis",
        "original_rank": 6,
        "adjusted_rank": 7.1,
        "total_frames_won": 47,
        "total_frames_lost": 34,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 13,
                "frames_lost": 17
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 3
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Edgar Diaz",
        "team": "Shotskis",
        "original_rank": 3,
        "adjusted_rank": 2.7,
        "total_frames_won": 30,
        "total_frames_lost": 23,
        "total_matches_won": 6,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Taylor Crossland",
        "team": "Shotskis",
        "original_rank": 4,
        "adjusted_rank": 3.5,
        "total_frames_won": 41,
        "total_frames_lost": 38,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Aditya Jha",
        "team": "Shotskis",
        "original_rank": 3,
        "adjusted_rank": 1.6,
        "total_frames_won": 12,
        "total_frames_lost": 22,
        "total_matches_won": 2,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Joshua Lebedinsky",
        "team": "Shotskis",
        "original_rank": 6,
        "adjusted_rank": 4.4,
        "total_frames_won": 54,
        "total_frames_lost": 65,
        "total_matches_won": 5,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 19
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 3,
                "frames_won": 27,
                "frames_lost": 28
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "John Kerbawy",
        "team": "Rack Appreciation Society",
        "original_rank": 8,
        "adjusted_rank": 10.5,
        "total_frames_won": 30,
        "total_frames_lost": 18,
        "total_matches_won": 4,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Miles Gordon",
        "team": "Rack Appreciation Society",
        "original_rank": 5,
        "adjusted_rank": 5.7,
        "total_frames_won": 36,
        "total_frames_lost": 31,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 17,
                "frames_lost": 19
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Armando Ramos",
        "team": "Rack Appreciation Society",
        "original_rank": 7,
        "adjusted_rank": 6.9,
        "total_frames_won": 29,
        "total_frames_lost": 41,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 17,
                "frames_lost": 24
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 12,
                "frames_lost": 17
            }
        }
    },
    {
        "name": "Nick Sanfardino",
        "team": "Rack Appreciation Society",
        "original_rank": 6,
        "adjusted_rank": 9.7,
        "total_frames_won": 62,
        "total_frames_lost": 39,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Mike Manney",
        "team": "Rack Appreciation Society",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 11,
        "total_frames_lost": 18,
        "total_matches_won": 1,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Ethan Nguyen",
        "team": "Rack Appreciation Society",
        "original_rank": 5,
        "adjusted_rank": 5.3,
        "total_frames_won": 22,
        "total_frames_lost": 20,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Rommel Alama",
        "team": "Rack Appreciation Society",
        "original_rank": 7,
        "adjusted_rank": 6.8,
        "total_frames_won": 28,
        "total_frames_lost": 40,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 18
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Eric Biddulphwest",
        "team": "Rack Appreciation Society",
        "original_rank": 5,
        "adjusted_rank": 5.4,
        "total_frames_won": 27,
        "total_frames_lost": 22,
        "total_matches_won": 3,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Charles Brunold",
        "team": "No Safeties",
        "original_rank": 7,
        "adjusted_rank": 9.0,
        "total_frames_won": 41,
        "total_frames_lost": 36,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 21,
                "frames_lost": 20
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Elena Walker",
        "team": "No Safeties",
        "original_rank": 5,
        "adjusted_rank": 4.8,
        "total_frames_won": 28,
        "total_frames_lost": 38,
        "total_matches_won": 2,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 11,
                "frames_lost": 15
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "John Moon (Forfeit)",
        "team": "No Safeties",
        "original_rank": 7,
        "adjusted_rank": 6.9,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Spencer Smith",
        "team": "No Safeties",
        "original_rank": 6,
        "adjusted_rank": 7.9,
        "total_frames_won": 51,
        "total_frames_lost": 39,
        "total_matches_won": 8,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 15
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "John Moon",
        "team": "No Safeties",
        "original_rank": 7,
        "adjusted_rank": 8.3,
        "total_frames_won": 48,
        "total_frames_lost": 43,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 19,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Jason Sam",
        "team": "No Safeties",
        "original_rank": 8,
        "adjusted_rank": 12.2,
        "total_frames_won": 60,
        "total_frames_lost": 45,
        "total_matches_won": 8,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            },
            "3": {
                "rank": 3,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 21,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 9
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Daniel Micher",
        "team": "No Safeties",
        "original_rank": 5,
        "adjusted_rank": 3.9,
        "total_frames_won": 32,
        "total_frames_lost": 47,
        "total_matches_won": 2,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 6,
                "frames_won": 23,
                "frames_lost": 39
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Nicholas Hofbauer",
        "team": "Always Going For The Nine",
        "original_rank": 6,
        "adjusted_rank": 7.2,
        "total_frames_won": 37,
        "total_frames_lost": 34,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 15
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 9
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Adrian Hiotis",
        "team": "Always Going For The Nine",
        "original_rank": 5,
        "adjusted_rank": 6.3,
        "total_frames_won": 30,
        "total_frames_lost": 12,
        "total_matches_won": 5,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 19,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Olivia Truong",
        "team": "Always Going For The Nine",
        "original_rank": 4,
        "adjusted_rank": 1.3,
        "total_frames_won": 19,
        "total_frames_lost": 42,
        "total_matches_won": 0,
        "total_matches_lost": 9,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 2,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 7,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Mark Kachelries",
        "team": "Always Going For The Nine",
        "original_rank": 6,
        "adjusted_rank": 7.4,
        "total_frames_won": 41,
        "total_frames_lost": 36,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Eddie Fortin (Forfeit)",
        "team": "Always Going For The Nine",
        "original_rank": 5,
        "adjusted_rank": 5.5,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Mindy Leslie",
        "team": "Always Going For The Nine",
        "original_rank": 6,
        "adjusted_rank": 5.0,
        "total_frames_won": 30,
        "total_frames_lost": 48,
        "total_matches_won": 2,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 4,
                "frames_won": 19,
                "frames_lost": 32
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Eddie Fortin",
        "team": "Always Going For The Nine",
        "original_rank": 5,
        "adjusted_rank": 5.9,
        "total_frames_won": 36,
        "total_frames_lost": 29,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 13
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Nick Owens",
        "team": "Always Going For The Nine",
        "original_rank": 5,
        "adjusted_rank": 3.8,
        "total_frames_won": 20,
        "total_frames_lost": 35,
        "total_matches_won": 1,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Rahul Keyal",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 1.8,
        "total_frames_won": 16,
        "total_frames_lost": 16,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Jean Louis Leroy",
        "team": "Better Call Sean",
        "original_rank": 6,
        "adjusted_rank": 3.7,
        "total_frames_won": 32,
        "total_frames_lost": 60,
        "total_matches_won": 0,
        "total_matches_lost": 10,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 12,
                "frames_lost": 19
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 7,
                "frames_lost": 19
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Brian Maher",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 2.6,
        "total_frames_won": 7,
        "total_frames_lost": 6,
        "total_matches_won": 1,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Lise Ho",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 1.5,
        "total_frames_won": 25,
        "total_frames_lost": 28,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Jean Louis Leroy (Forfeit)",
        "team": "Better Call Sean",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Mario Longobardi (Forfeit)",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 3.4,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Ben Groh (Forfeit)",
        "team": "Better Call Sean",
        "original_rank": 4,
        "adjusted_rank": 4.5,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Rahul Keyal (Forfeit)",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 3.4,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Sandeep Sunny",
        "team": "Better Call Sean",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 50,
        "total_frames_lost": 46,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 8
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 10
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Ben Groh",
        "team": "Better Call Sean",
        "original_rank": 4,
        "adjusted_rank": 2.6,
        "total_frames_won": 24,
        "total_frames_lost": 33,
        "total_matches_won": 1,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 11,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Mario Longobardi",
        "team": "Better Call Sean",
        "original_rank": 3,
        "adjusted_rank": 1.5,
        "total_frames_won": 26,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 6
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Adentunji Shennaike",
        "team": "The Bloomie B List",
        "original_rank": 3,
        "adjusted_rank": 2.0,
        "total_frames_won": 26,
        "total_frames_lost": 23,
        "total_matches_won": 5,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Nicholas Baldaro",
        "team": "The Bloomie B List",
        "original_rank": 3,
        "adjusted_rank": 0.2,
        "total_frames_won": 26,
        "total_frames_lost": 38,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 13,
                "frames_lost": 17
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Pete Siki",
        "team": "The Bloomie B List",
        "original_rank": 4,
        "adjusted_rank": 2.8,
        "total_frames_won": 4,
        "total_frames_lost": 13,
        "total_matches_won": 1,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 0,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Julian Haresco",
        "team": "The Bloomie B List",
        "original_rank": 4,
        "adjusted_rank": 0.4,
        "total_frames_won": 22,
        "total_frames_lost": 46,
        "total_matches_won": 1,
        "total_matches_lost": 9,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 16
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 8,
                "frames_lost": 19
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Adrian Gaurila",
        "team": "The Bloomie B List",
        "original_rank": 4,
        "adjusted_rank": 1.6,
        "total_frames_won": 25,
        "total_frames_lost": 39,
        "total_matches_won": 3,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 12,
                "frames_lost": 16
            }
        }
    },
    {
        "name": "Ronald Cajigas",
        "team": "The Bloomie B List",
        "original_rank": 3,
        "adjusted_rank": -0.3,
        "total_frames_won": 27,
        "total_frames_lost": 43,
        "total_matches_won": 4,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 12
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Abder Mihoubi",
        "team": "The Bloomie B List",
        "original_rank": 4,
        "adjusted_rank": 2.0,
        "total_frames_won": 13,
        "total_frames_lost": 24,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Nick Makes",
        "team": "Shake And Break",
        "original_rank": 8,
        "adjusted_rank": 10.7,
        "total_frames_won": 46,
        "total_frames_lost": 53,
        "total_matches_won": 3,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 18,
                "frames_lost": 21
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Jamie Anderson",
        "team": "Shake And Break",
        "original_rank": 3,
        "adjusted_rank": 1.7,
        "total_frames_won": 30,
        "total_frames_lost": 32,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 19,
                "frames_lost": 18
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Jordan Tse",
        "team": "Shake And Break",
        "original_rank": 3,
        "adjusted_rank": 1.9,
        "total_frames_won": 14,
        "total_frames_lost": 21,
        "total_matches_won": 0,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Tyler Kaye",
        "team": "Shake And Break",
        "original_rank": 5,
        "adjusted_rank": 5.5,
        "total_frames_won": 21,
        "total_frames_lost": 17,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Mike OBrien",
        "team": "Shake And Break",
        "original_rank": 5,
        "adjusted_rank": 4.6,
        "total_frames_won": 8,
        "total_frames_lost": 22,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 4,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Angela Snowton",
        "team": "Shake And Break",
        "original_rank": 3,
        "adjusted_rank": 1.7,
        "total_frames_won": 9,
        "total_frames_lost": 18,
        "total_matches_won": 1,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Mo Takao",
        "team": "Shake And Break",
        "original_rank": 7,
        "adjusted_rank": 7.4,
        "total_frames_won": 35,
        "total_frames_lost": 46,
        "total_matches_won": 2,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 12,
                "frames_lost": 19
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Kendall Nunn",
        "team": "Shake And Break",
        "original_rank": 7,
        "adjusted_rank": 10.3,
        "total_frames_won": 61,
        "total_frames_lost": 42,
        "total_matches_won": 7,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 16,
                "frames_lost": 17
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 25,
                "frames_lost": 15
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Jeff Diers",
        "team": "The Eight Makers",
        "original_rank": 5,
        "adjusted_rank": 3.8,
        "total_frames_won": 23,
        "total_frames_lost": 36,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Jennifer Mary",
        "team": "The Eight Makers",
        "original_rank": 3,
        "adjusted_rank": 1.9,
        "total_frames_won": 25,
        "total_frames_lost": 28,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 12,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Dagm Zegeye",
        "team": "The Eight Makers",
        "original_rank": 5,
        "adjusted_rank": 3.8,
        "total_frames_won": 22,
        "total_frames_lost": 37,
        "total_matches_won": 0,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 9,
                "frames_lost": 12
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Thuy Tran",
        "team": "The Eight Makers",
        "original_rank": 4,
        "adjusted_rank": 3.0,
        "total_frames_won": 32,
        "total_frames_lost": 28,
        "total_matches_won": 5,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Seth Rubin",
        "team": "The Eight Makers",
        "original_rank": 4,
        "adjusted_rank": 1.1,
        "total_frames_won": 18,
        "total_frames_lost": 35,
        "total_matches_won": 0,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 9,
                "frames_lost": 14
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 6,
                "frames_lost": 14
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Merril Jeffs",
        "team": "The Eight Makers",
        "original_rank": 5,
        "adjusted_rank": 4.8,
        "total_frames_won": 20,
        "total_frames_lost": 27,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 7,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Shan Sengottaiyan",
        "team": "The Eight Makers",
        "original_rank": 5,
        "adjusted_rank": 4.5,
        "total_frames_won": 23,
        "total_frames_lost": 27,
        "total_matches_won": 1,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 8,
                "frames_lost": 14
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Sabine Lafleur",
        "team": "The Eight Makers",
        "original_rank": 3,
        "adjusted_rank": -0.0,
        "total_frames_won": 14,
        "total_frames_lost": 28,
        "total_matches_won": 0,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 8,
                "frames_lost": 15
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Dario Tapia",
        "team": "Ball Droppers",
        "original_rank": 9,
        "adjusted_rank": 11.8,
        "total_frames_won": 48,
        "total_frames_lost": 52,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 4,
                "frames_won": 21,
                "frames_lost": 28
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Gabby Santana",
        "team": "Ball Droppers",
        "original_rank": 4,
        "adjusted_rank": 3.4,
        "total_frames_won": 23,
        "total_frames_lost": 20,
        "total_matches_won": 3,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Tom Martin",
        "team": "Ball Droppers",
        "original_rank": 6,
        "adjusted_rank": 5.8,
        "total_frames_won": 4,
        "total_frames_lost": 10,
        "total_matches_won": 0,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 10
            }
        }
    },
    {
        "name": "Carmelo Andujar",
        "team": "Ball Droppers",
        "original_rank": 7,
        "adjusted_rank": 9.3,
        "total_frames_won": 57,
        "total_frames_lost": 43,
        "total_matches_won": 7,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 5
            },
            "8": {
                "rank": 8,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 2
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 17
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 21,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Madeleine Wilson",
        "team": "Ball Droppers",
        "original_rank": 4,
        "adjusted_rank": 4.0,
        "total_frames_won": 29,
        "total_frames_lost": 18,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Theresa Hong",
        "team": "Ball Droppers",
        "original_rank": 4,
        "adjusted_rank": 3.6,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Katya Slepoy",
        "team": "Ball Droppers",
        "original_rank": 4,
        "adjusted_rank": 5.6,
        "total_frames_won": 51,
        "total_frames_lost": 14,
        "total_matches_won": 10,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 1
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Luis Ortiz",
        "team": "Ball Droppers",
        "original_rank": 8,
        "adjusted_rank": 9.2,
        "total_frames_won": 27,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Dario Tapia (Forfeit)",
        "team": "Ball Droppers",
        "original_rank": 9,
        "adjusted_rank": 10.2,
        "total_frames_won": 7,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Luis Ortiz (Forfeit)",
        "team": "Ball Droppers",
        "original_rank": 8,
        "adjusted_rank": 9.1,
        "total_frames_won": 7,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Carmelo Andujar (Forfeit)",
        "team": "Ball Droppers",
        "original_rank": 7,
        "adjusted_rank": 8.0,
        "total_frames_won": 7,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Katya Slepoy (Forfeit)",
        "team": "Ball Droppers",
        "original_rank": 2,
        "adjusted_rank": 2.3,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Madeleine Wilson (Forfeit)",
        "team": "Ball Droppers",
        "original_rank": 4,
        "adjusted_rank": 3.4,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Paul Gossman",
        "team": "Hot Pockets",
        "original_rank": 7,
        "adjusted_rank": 9.4,
        "total_frames_won": 42,
        "total_frames_lost": 30,
        "total_matches_won": 5,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 14
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "David Crandall",
        "team": "Hot Pockets",
        "original_rank": 4,
        "adjusted_rank": 3.8,
        "total_frames_won": 36,
        "total_frames_lost": 29,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Aaron Lewis",
        "team": "Hot Pockets",
        "original_rank": 5,
        "adjusted_rank": 5.9,
        "total_frames_won": 50,
        "total_frames_lost": 45,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 12,
                "frames_lost": 16
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 12,
                "frames_lost": 10
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 8
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 6
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Joey Shurtleff",
        "team": "Hot Pockets",
        "original_rank": 5,
        "adjusted_rank": 5.8,
        "total_frames_won": 22,
        "total_frames_lost": 14,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 17,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Julia Opatrny",
        "team": "Hot Pockets",
        "original_rank": 2,
        "adjusted_rank": -0.8,
        "total_frames_won": 35,
        "total_frames_lost": 36,
        "total_matches_won": 5,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 16,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 9
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Tim Burns",
        "team": "Hot Pockets",
        "original_rank": 7,
        "adjusted_rank": 9.7,
        "total_frames_won": 62,
        "total_frames_lost": 43,
        "total_matches_won": 8,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 17,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 21,
                "frames_lost": 19
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Noon Chan",
        "team": "Demon Time",
        "original_rank": 2,
        "adjusted_rank": 1.8,
        "total_frames_won": 10,
        "total_frames_lost": 9,
        "total_matches_won": 1,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Spencer Charles",
        "team": "Demon Time",
        "original_rank": 3,
        "adjusted_rank": 2.7,
        "total_frames_won": 3,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Flomary Swensen",
        "team": "Demon Time",
        "original_rank": 4,
        "adjusted_rank": 2.4,
        "total_frames_won": 32,
        "total_frames_lost": 39,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 9
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Eazy Laster",
        "team": "Demon Time",
        "original_rank": 5,
        "adjusted_rank": 7.6,
        "total_frames_won": 77,
        "total_frames_lost": 45,
        "total_matches_won": 11,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 28,
                "frames_lost": 17
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 19,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Jason Robinson",
        "team": "Demon Time",
        "original_rank": 6,
        "adjusted_rank": 8.3,
        "total_frames_won": 45,
        "total_frames_lost": 30,
        "total_matches_won": 6,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 16,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 14
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Will Moore",
        "team": "Demon Time",
        "original_rank": 5,
        "adjusted_rank": 4.3,
        "total_frames_won": 16,
        "total_frames_lost": 24,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 10
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Iris Chang",
        "team": "Demon Time",
        "original_rank": 3,
        "adjusted_rank": 2.9,
        "total_frames_won": 51,
        "total_frames_lost": 34,
        "total_matches_won": 10,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 17,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Bruce Kleiman",
        "team": "I'd Hit That",
        "original_rank": 7,
        "adjusted_rank": 6.4,
        "total_frames_won": 28,
        "total_frames_lost": 37,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 11,
                "frames_lost": 20
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Jason Skipper",
        "team": "I'd Hit That",
        "original_rank": 6,
        "adjusted_rank": 7.8,
        "total_frames_won": 56,
        "total_frames_lost": 42,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 25,
                "frames_lost": 21
            },
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 2,
                "frames_won": 26,
                "frames_lost": 20
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "John Doucette",
        "team": "I'd Hit That",
        "original_rank": 6,
        "adjusted_rank": 8.7,
        "total_frames_won": 51,
        "total_frames_lost": 32,
        "total_matches_won": 7,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 18,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 17,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Kevin Glick",
        "team": "I'd Hit That",
        "original_rank": 7,
        "adjusted_rank": 7.1,
        "total_frames_won": 23,
        "total_frames_lost": 28,
        "total_matches_won": 2,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 19
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Patricia Arroyo",
        "team": "I'd Hit That",
        "original_rank": 4,
        "adjusted_rank": 5.3,
        "total_frames_won": 27,
        "total_frames_lost": 16,
        "total_matches_won": 5,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 4,
                "matches_lost": 1,
                "frames_won": 23,
                "frames_lost": 13
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Glenn Warnecke",
        "team": "I'd Hit That",
        "original_rank": 5,
        "adjusted_rank": 6.0,
        "total_frames_won": 33,
        "total_frames_lost": 29,
        "total_matches_won": 6,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 2,
                "frames_won": 22,
                "frames_lost": 19
            }
        }
    },
    {
        "name": "Mark Barranco",
        "team": "I'd Hit That",
        "original_rank": 6,
        "adjusted_rank": 9.2,
        "total_frames_won": 43,
        "total_frames_lost": 23,
        "total_matches_won": 7,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Natalie Tsvetkova (Forfeit)",
        "team": "MonGods",
        "original_rank": 3,
        "adjusted_rank": 3.1,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Paul Aldana",
        "team": "MonGods",
        "original_rank": 5,
        "adjusted_rank": 4.5,
        "total_frames_won": 35,
        "total_frames_lost": 36,
        "total_matches_won": 5,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Wenqin Ye",
        "team": "MonGods",
        "original_rank": 3,
        "adjusted_rank": 2.1,
        "total_frames_won": 7,
        "total_frames_lost": 11,
        "total_matches_won": 1,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Jason Ngassa",
        "team": "MonGods",
        "original_rank": 4,
        "adjusted_rank": 3.2,
        "total_frames_won": 7,
        "total_frames_lost": 15,
        "total_matches_won": 0,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Jonathan Lee",
        "team": "MonGods",
        "original_rank": 4,
        "adjusted_rank": 3.2,
        "total_frames_won": 48,
        "total_frames_lost": 37,
        "total_matches_won": 7,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 11
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Thomas Tran",
        "team": "MonGods",
        "original_rank": 4,
        "adjusted_rank": 4.8,
        "total_frames_won": 48,
        "total_frames_lost": 32,
        "total_matches_won": 8,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 3
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Natalie Tsvetkova",
        "team": "MonGods",
        "original_rank": 3,
        "adjusted_rank": 1.3,
        "total_frames_won": 27,
        "total_frames_lost": 32,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 9
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Andrew Chen",
        "team": "MonGods",
        "original_rank": 4,
        "adjusted_rank": 3.7,
        "total_frames_won": 47,
        "total_frames_lost": 35,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 6
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "John Bates",
        "team": "Pocketeers",
        "original_rank": 6,
        "adjusted_rank": 7.6,
        "total_frames_won": 48,
        "total_frames_lost": 34,
        "total_matches_won": 7,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 18,
                "frames_lost": 22
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 0,
                "frames_won": 25,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Kim Mcadams",
        "team": "Pocketeers",
        "original_rank": 6,
        "adjusted_rank": 7.1,
        "total_frames_won": 59,
        "total_frames_lost": 49,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 22,
                "frames_lost": 16
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 16
            },
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 24,
                "frames_lost": 16
            }
        }
    },
    {
        "name": "Julio Pena",
        "team": "Pocketeers",
        "original_rank": 7,
        "adjusted_rank": 7.5,
        "total_frames_won": 22,
        "total_frames_lost": 24,
        "total_matches_won": 2,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "Kristie Lim",
        "team": "Pocketeers",
        "original_rank": 3,
        "adjusted_rank": 2.5,
        "total_frames_won": 49,
        "total_frames_lost": 35,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 12,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Valerie Bennett",
        "team": "Pocketeers",
        "original_rank": 5,
        "adjusted_rank": 4.9,
        "total_frames_won": 24,
        "total_frames_lost": 28,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Fabian Marquez",
        "team": "Pocketeers",
        "original_rank": 7,
        "adjusted_rank": 6.4,
        "total_frames_won": 1,
        "total_frames_lost": 7,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Hal Klinger",
        "team": "Pocketeers",
        "original_rank": 5,
        "adjusted_rank": 6.3,
        "total_frames_won": 39,
        "total_frames_lost": 31,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Vinny Merolla",
        "team": "Ready On Cue",
        "original_rank": 4,
        "adjusted_rank": 3.2,
        "total_frames_won": 20,
        "total_frames_lost": 25,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 12
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Justin Lozano",
        "team": "Ready On Cue",
        "original_rank": 4,
        "adjusted_rank": 4.2,
        "total_frames_won": 22,
        "total_frames_lost": 23,
        "total_matches_won": 4,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 2,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Justin Chang",
        "team": "Ready On Cue",
        "original_rank": 8,
        "adjusted_rank": 10.4,
        "total_frames_won": 57,
        "total_frames_lost": 62,
        "total_matches_won": 5,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 25,
                "frames_lost": 26
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 12,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Shubh Varma",
        "team": "Ready On Cue",
        "original_rank": 5,
        "adjusted_rank": 5.3,
        "total_frames_won": 24,
        "total_frames_lost": 27,
        "total_matches_won": 2,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 7,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Gene Heinrich",
        "team": "Ready On Cue",
        "original_rank": 8,
        "adjusted_rank": 11.8,
        "total_frames_won": 60,
        "total_frames_lost": 57,
        "total_matches_won": 6,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 22,
                "frames_lost": 23
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Gene Demo",
        "team": "Ready On Cue",
        "original_rank": 5,
        "adjusted_rank": 6.4,
        "total_frames_won": 43,
        "total_frames_lost": 33,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 11,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 16,
                "frames_lost": 14
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Michael OBeirne (Forfeit)",
        "team": "Continue Break",
        "original_rank": 4,
        "adjusted_rank": 4.3,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Adam Norton",
        "team": "Continue Break",
        "original_rank": 7,
        "adjusted_rank": 8.0,
        "total_frames_won": 20,
        "total_frames_lost": 16,
        "total_matches_won": 3,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Rebecca Gu",
        "team": "Continue Break",
        "original_rank": 4,
        "adjusted_rank": 2.8,
        "total_frames_won": 14,
        "total_frames_lost": 24,
        "total_matches_won": 2,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 11
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Michael Yan",
        "team": "Continue Break",
        "original_rank": 6,
        "adjusted_rank": 8.7,
        "total_frames_won": 53,
        "total_frames_lost": 38,
        "total_matches_won": 8,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 12
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 4,
                "matches_lost": 2,
                "frames_won": 24,
                "frames_lost": 15
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Aiden Xiao",
        "team": "Continue Break",
        "original_rank": 7,
        "adjusted_rank": 5.9,
        "total_frames_won": 40,
        "total_frames_lost": 58,
        "total_matches_won": 3,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 18,
                "frames_lost": 21
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 18
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Eddy Wang",
        "team": "Continue Break",
        "original_rank": 6,
        "adjusted_rank": 8.0,
        "total_frames_won": 37,
        "total_frames_lost": 25,
        "total_matches_won": 5,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 25,
                "frames_lost": 15
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Michael OBeirne",
        "team": "Continue Break",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 31,
        "total_frames_lost": 30,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 12
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ben Kiefer",
        "team": "Continue Break",
        "original_rank": 3,
        "adjusted_rank": 0.6,
        "total_frames_won": 30,
        "total_frames_lost": 34,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 11,
                "frames_lost": 16
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Mike Laterza",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 3.1,
        "total_frames_won": 33,
        "total_frames_lost": 36,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Matt Moses",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 3.8,
        "total_frames_won": 33,
        "total_frames_lost": 32,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Mike Laterza (Forfeit)",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 2.5,
        "total_frames_won": 0,
        "total_frames_lost": 15,
        "total_matches_won": 0,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 0,
                "frames_lost": 10
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ryan Segal",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 3.0,
        "total_frames_won": 12,
        "total_frames_lost": 15,
        "total_matches_won": 1,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Jordan Essinger",
        "team": "Weekend Warriors",
        "original_rank": 3,
        "adjusted_rank": 1.5,
        "total_frames_won": 26,
        "total_frames_lost": 28,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Mike Spaeth (Forfeit)",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 2.1,
        "total_frames_won": 0,
        "total_frames_lost": 17,
        "total_matches_won": 0,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 0,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Mike Spaeth",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 3.3,
        "total_frames_won": 29,
        "total_frames_lost": 26,
        "total_matches_won": 5,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Matt Moses (Forfeit)",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 2.1,
        "total_frames_won": 0,
        "total_frames_lost": 17,
        "total_matches_won": 0,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Pat Lebuhn (Forfeit)",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 1.7,
        "total_frames_won": 0,
        "total_frames_lost": 17,
        "total_matches_won": 0,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Pat Lebuhn",
        "team": "Weekend Warriors",
        "original_rank": 4,
        "adjusted_rank": 1.5,
        "total_frames_won": 26,
        "total_frames_lost": 38,
        "total_matches_won": 2,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 19,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 8
            }
        }
    },
    {
        "name": "Izzo Castillo (Forfeit)",
        "team": "Super Billiards Brothers",
        "original_rank": 6,
        "adjusted_rank": 5.7,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Kartikey Grover",
        "team": "Super Billiards Brothers",
        "original_rank": 7,
        "adjusted_rank": 7.7,
        "total_frames_won": 7,
        "total_frames_lost": 2,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "John Kang",
        "team": "Super Billiards Brothers",
        "original_rank": 6,
        "adjusted_rank": 5.8,
        "total_frames_won": 37,
        "total_frames_lost": 43,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 11,
                "frames_lost": 20
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Steven The",
        "team": "Super Billiards Brothers",
        "original_rank": 5,
        "adjusted_rank": 5.9,
        "total_frames_won": 45,
        "total_frames_lost": 36,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 3,
                "frames_won": 27,
                "frames_lost": 26
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Izzo Castillo",
        "team": "Super Billiards Brothers",
        "original_rank": 6,
        "adjusted_rank": 7.0,
        "total_frames_won": 43,
        "total_frames_lost": 40,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 22,
                "frames_lost": 19
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "John Kang (Forfeit)",
        "team": "Super Billiards Brothers",
        "original_rank": 6,
        "adjusted_rank": 5.4,
        "total_frames_won": 0,
        "total_frames_lost": 7,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Ramesh Torres",
        "team": "Super Billiards Brothers",
        "original_rank": 6,
        "adjusted_rank": 5.9,
        "total_frames_won": 73,
        "total_frames_lost": 87,
        "total_matches_won": 7,
        "total_matches_lost": 11,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 5,
                "frames_won": 22,
                "frames_lost": 36
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 4,
                "frames_won": 20,
                "frames_lost": 28
            },
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 17,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Neil Hickey",
        "team": "Super Billiards Brothers",
        "original_rank": 7,
        "adjusted_rank": 8.3,
        "total_frames_won": 37,
        "total_frames_lost": 30,
        "total_matches_won": 4,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 15
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "Jane Nechayevsky",
        "team": "Rack N Rollers",
        "original_rank": 2,
        "adjusted_rank": -1.3,
        "total_frames_won": 30,
        "total_frames_lost": 33,
        "total_matches_won": 3,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 19,
                "frames_lost": 16
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Sherrie Mark",
        "team": "Rack N Rollers",
        "original_rank": 3,
        "adjusted_rank": 1.7,
        "total_frames_won": 19,
        "total_frames_lost": 24,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Aaron Pope",
        "team": "Rack N Rollers",
        "original_rank": 4,
        "adjusted_rank": 1.8,
        "total_frames_won": 28,
        "total_frames_lost": 42,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 13,
                "frames_lost": 21
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Henry Chavez",
        "team": "Rack N Rollers",
        "original_rank": 4,
        "adjusted_rank": 3.0,
        "total_frames_won": 31,
        "total_frames_lost": 29,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 7,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Joel Gonzalez",
        "team": "Rack N Rollers",
        "original_rank": 6,
        "adjusted_rank": 6.1,
        "total_frames_won": 64,
        "total_frames_lost": 63,
        "total_matches_won": 8,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 13,
                "frames_lost": 20
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 17
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 12
            },
            "8": {
                "rank": 8,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Emmit Flynn",
        "team": "Rack N Rollers",
        "original_rank": 4,
        "adjusted_rank": 4.3,
        "total_frames_won": 24,
        "total_frames_lost": 19,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Emmit Flynn (Forfeit)",
        "team": "Rack N Rollers",
        "original_rank": 4,
        "adjusted_rank": 3.5,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Tony Pecora",
        "team": "Ballz 2 The Wall",
        "original_rank": 6,
        "adjusted_rank": 3.8,
        "total_frames_won": 38,
        "total_frames_lost": 66,
        "total_matches_won": 1,
        "total_matches_lost": 10,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 14,
                "frames_lost": 20
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 11,
                "frames_lost": 26
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Dennis Gibbons",
        "team": "Ballz 2 The Wall",
        "original_rank": 5,
        "adjusted_rank": 4.2,
        "total_frames_won": 39,
        "total_frames_lost": 49,
        "total_matches_won": 5,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 17,
                "frames_lost": 16
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 4,
                "frames_won": 7,
                "frames_lost": 21
            }
        }
    },
    {
        "name": "Jerry Teicht",
        "team": "Ballz 2 The Wall",
        "original_rank": 6,
        "adjusted_rank": 5.6,
        "total_frames_won": 70,
        "total_frames_lost": 76,
        "total_matches_won": 7,
        "total_matches_lost": 9,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 5,
                "frames_won": 18,
                "frames_lost": 39
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 30,
                "frames_lost": 19
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ross Zeltzer",
        "team": "Ballz 2 The Wall",
        "original_rank": 5,
        "adjusted_rank": 6.3,
        "total_frames_won": 34,
        "total_frames_lost": 25,
        "total_matches_won": 6,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "John LaMura",
        "team": "Ballz 2 The Wall",
        "original_rank": 3,
        "adjusted_rank": 2.3,
        "total_frames_won": 37,
        "total_frames_lost": 26,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Frank Fico",
        "team": "MYOB",
        "original_rank": 7,
        "adjusted_rank": 7.7,
        "total_frames_won": 29,
        "total_frames_lost": 40,
        "total_matches_won": 2,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 20,
                "frames_lost": 17
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 9
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Richard Constable",
        "team": "MYOB",
        "original_rank": 7,
        "adjusted_rank": 6.6,
        "total_frames_won": 21,
        "total_frames_lost": 32,
        "total_matches_won": 1,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Vidhya Kamdar",
        "team": "MYOB",
        "original_rank": 2,
        "adjusted_rank": 0.3,
        "total_frames_won": 15,
        "total_frames_lost": 25,
        "total_matches_won": 1,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 11
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Allison LaFleur",
        "team": "MYOB",
        "original_rank": 7,
        "adjusted_rank": 9.1,
        "total_frames_won": 33,
        "total_frames_lost": 21,
        "total_matches_won": 4,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Kimberly Fontanilla",
        "team": "MYOB",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 28,
        "total_frames_lost": 37,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 14,
                "frames_lost": 18
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "James Killen",
        "team": "MYOB",
        "original_rank": 6,
        "adjusted_rank": 4.6,
        "total_frames_won": 25,
        "total_frames_lost": 44,
        "total_matches_won": 1,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 9,
                "frames_lost": 17
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Inessa Gelman",
        "team": "MYOB",
        "original_rank": 6,
        "adjusted_rank": 8.2,
        "total_frames_won": 37,
        "total_frames_lost": 25,
        "total_matches_won": 6,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 18,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Sara Firestone",
        "team": "MYOB",
        "original_rank": 6,
        "adjusted_rank": 6.6,
        "total_frames_won": 26,
        "total_frames_lost": 31,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 14,
                "frames_lost": 19
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "James Brinnen",
        "team": "4 Q People",
        "original_rank": 5,
        "adjusted_rank": 4.0,
        "total_frames_won": 44,
        "total_frames_lost": 49,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 4,
                "frames_won": 30,
                "frames_lost": 32
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Joseph Kleinman",
        "team": "4 Q People",
        "original_rank": 6,
        "adjusted_rank": 6.6,
        "total_frames_won": 43,
        "total_frames_lost": 49,
        "total_matches_won": 4,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 6
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 12
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Alex Franchilli",
        "team": "4 Q People",
        "original_rank": 5,
        "adjusted_rank": 4.2,
        "total_frames_won": 49,
        "total_frames_lost": 55,
        "total_matches_won": 5,
        "total_matches_lost": 8,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 3,
                "frames_won": 21,
                "frames_lost": 21
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 18
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Shi Chen",
        "team": "4 Q People",
        "original_rank": 4,
        "adjusted_rank": 4.6,
        "total_frames_won": 46,
        "total_frames_lost": 36,
        "total_matches_won": 9,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Lenn Bryant",
        "team": "4 Q People",
        "original_rank": 5,
        "adjusted_rank": 2.8,
        "total_frames_won": 33,
        "total_frames_lost": 47,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 15
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 14
            }
        }
    },
    {
        "name": "Mickal Famorca",
        "team": "Rich Strikers",
        "original_rank": 5,
        "adjusted_rank": 5.2,
        "total_frames_won": 40,
        "total_frames_lost": 32,
        "total_matches_won": 7,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 14,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Jonathan Tirrell",
        "team": "Rich Strikers",
        "original_rank": 5,
        "adjusted_rank": 6.4,
        "total_frames_won": 34,
        "total_frames_lost": 21,
        "total_matches_won": 6,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Teddy Ellison",
        "team": "Rich Strikers",
        "original_rank": 5,
        "adjusted_rank": 4.2,
        "total_frames_won": 26,
        "total_frames_lost": 30,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 14
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Charles ONeill",
        "team": "Rich Strikers",
        "original_rank": 4,
        "adjusted_rank": 4.4,
        "total_frames_won": 32,
        "total_frames_lost": 22,
        "total_matches_won": 5,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Christian Johnson",
        "team": "Rich Strikers",
        "original_rank": 6,
        "adjusted_rank": 5.9,
        "total_frames_won": 34,
        "total_frames_lost": 41,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 8,
                "frames_lost": 21
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Brett Schreiber",
        "team": "Rich Strikers",
        "original_rank": 4,
        "adjusted_rank": 2.6,
        "total_frames_won": 27,
        "total_frames_lost": 35,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 12
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Sara Goldman",
        "team": "Rich Strikers",
        "original_rank": 3,
        "adjusted_rank": 1.4,
        "total_frames_won": 27,
        "total_frames_lost": 29,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 6,
                "frames_lost": 8
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Angelo Quadara",
        "team": "Wild Nine West",
        "original_rank": 9,
        "adjusted_rank": 12.0,
        "total_frames_won": 43,
        "total_frames_lost": 31,
        "total_matches_won": 7,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 11,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 4,
                "matches_lost": 1,
                "frames_won": 30,
                "frames_lost": 22
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 2,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Julia Sacknoff",
        "team": "Wild Nine West",
        "original_rank": 4,
        "adjusted_rank": 3.7,
        "total_frames_won": 38,
        "total_frames_lost": 39,
        "total_matches_won": 5,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 15,
                "frames_lost": 18
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 8
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Ryan Chiu",
        "team": "Wild Nine West",
        "original_rank": 4,
        "adjusted_rank": 3.9,
        "total_frames_won": 27,
        "total_frames_lost": 22,
        "total_matches_won": 5,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 10
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Emmeline Chen",
        "team": "Wild Nine West",
        "original_rank": 4,
        "adjusted_rank": 3.5,
        "total_frames_won": 18,
        "total_frames_lost": 18,
        "total_matches_won": 2,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Daniel Ilibassi",
        "team": "Wild Nine West",
        "original_rank": 6,
        "adjusted_rank": 7.3,
        "total_frames_won": 39,
        "total_frames_lost": 30,
        "total_matches_won": 5,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 18,
                "frames_lost": 8
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 21,
                "frames_lost": 22
            }
        }
    },
    {
        "name": "Brandi Ripp",
        "team": "Wild Nine West",
        "original_rank": 3,
        "adjusted_rank": 0.6,
        "total_frames_won": 27,
        "total_frames_lost": 32,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Sanjid Dewan",
        "team": "Wild Nine West",
        "original_rank": 5,
        "adjusted_rank": 4.9,
        "total_frames_won": 42,
        "total_frames_lost": 41,
        "total_matches_won": 7,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 5,
                "matches_lost": 1,
                "frames_won": 25,
                "frames_lost": 16
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 17,
                "frames_lost": 20
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Mukesh Khurana",
        "team": "Straight Shooters",
        "original_rank": 5,
        "adjusted_rank": 3.6,
        "total_frames_won": 36,
        "total_frames_lost": 46,
        "total_matches_won": 3,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Mary Lenz",
        "team": "Straight Shooters",
        "original_rank": 4,
        "adjusted_rank": 3.5,
        "total_frames_won": 35,
        "total_frames_lost": 38,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 15
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "David Noah",
        "team": "Straight Shooters",
        "original_rank": 5,
        "adjusted_rank": 5.4,
        "total_frames_won": 20,
        "total_frames_lost": 17,
        "total_matches_won": 2,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Olivia Barbulescu",
        "team": "Straight Shooters",
        "original_rank": 2,
        "adjusted_rank": -0.4,
        "total_frames_won": 18,
        "total_frames_lost": 28,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 11
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Brian McGough",
        "team": "Straight Shooters",
        "original_rank": 5,
        "adjusted_rank": 5.7,
        "total_frames_won": 22,
        "total_frames_lost": 15,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Ryan Hall",
        "team": "Straight Shooters",
        "original_rank": 4,
        "adjusted_rank": 4.8,
        "total_frames_won": 24,
        "total_frames_lost": 16,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 11
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Jonathan Roth",
        "team": "Straight Shooters",
        "original_rank": 6,
        "adjusted_rank": 6.3,
        "total_frames_won": 47,
        "total_frames_lost": 49,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 17
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 9
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Landrew Gomes",
        "team": "Chalk -N- Bourbon",
        "original_rank": 7,
        "adjusted_rank": 8.3,
        "total_frames_won": 39,
        "total_frames_lost": 28,
        "total_matches_won": 5,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 25,
                "frames_lost": 15
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "9": {
                "rank": 9,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Jamie Piszak",
        "team": "Chalk -N- Bourbon",
        "original_rank": 5,
        "adjusted_rank": 4.8,
        "total_frames_won": 52,
        "total_frames_lost": 46,
        "total_matches_won": 5,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 28,
                "frames_lost": 21
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Max Schuster",
        "team": "Chalk -N- Bourbon",
        "original_rank": 3,
        "adjusted_rank": 3.9,
        "total_frames_won": 49,
        "total_frames_lost": 25,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 19,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 11
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Amaury Lozano",
        "team": "Chalk -N- Bourbon",
        "original_rank": 4,
        "adjusted_rank": 3.8,
        "total_frames_won": 33,
        "total_frames_lost": 32,
        "total_matches_won": 4,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 9
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Daniel Wright",
        "team": "Chalk -N- Bourbon",
        "original_rank": 4,
        "adjusted_rank": 4.1,
        "total_frames_won": 23,
        "total_frames_lost": 18,
        "total_matches_won": 3,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Jonathan Lindsay",
        "team": "Chalk -N- Bourbon",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 44,
        "total_frames_lost": 46,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 13
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 16
            }
        }
    },
    {
        "name": "Mary Murphy",
        "team": "Pickpockets",
        "original_rank": 7,
        "adjusted_rank": 8.1,
        "total_frames_won": 32,
        "total_frames_lost": 35,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 20
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            }
        }
    },
    {
        "name": "Johnny Osorio",
        "team": "Pickpockets",
        "original_rank": 8,
        "adjusted_rank": 12.2,
        "total_frames_won": 64,
        "total_frames_lost": 60,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 1,
                "frames_won": 27,
                "frames_lost": 18
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 14
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 8
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 11,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Simon NG",
        "team": "Pickpockets",
        "original_rank": 7,
        "adjusted_rank": 8.2,
        "total_frames_won": 41,
        "total_frames_lost": 44,
        "total_matches_won": 5,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 11
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 16,
                "frames_lost": 23
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Salvatore Russo (Forfeit)",
        "team": "Pickpockets",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 5,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Salvatore Russo",
        "team": "Pickpockets",
        "original_rank": 5,
        "adjusted_rank": 5.1,
        "total_frames_won": 43,
        "total_frames_lost": 50,
        "total_matches_won": 5,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 11
            },
            "3": {
                "rank": 3,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 16,
                "frames_lost": 19
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Lenny Bogdanov",
        "team": "Pickpockets",
        "original_rank": 8,
        "adjusted_rank": 11.3,
        "total_frames_won": 59,
        "total_frames_lost": 59,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 21
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 2,
                "frames_won": 32,
                "frames_lost": 28
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 3
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Andrew Russo",
        "team": "Pickpockets",
        "original_rank": 5,
        "adjusted_rank": 5.1,
        "total_frames_won": 15,
        "total_frames_lost": 16,
        "total_matches_won": 2,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Chelsea Ireland",
        "team": "Baby Sharks",
        "original_rank": 3,
        "adjusted_rank": -0.4,
        "total_frames_won": 38,
        "total_frames_lost": 47,
        "total_matches_won": 7,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 3,
                "frames_won": 16,
                "frames_lost": 22
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 10
            }
        }
    },
    {
        "name": "Arpan Patel (Forfeit)",
        "team": "Baby Sharks",
        "original_rank": 5,
        "adjusted_rank": 5.6,
        "total_frames_won": 7,
        "total_frames_lost": 0,
        "total_matches_won": 1,
        "total_matches_lost": 0,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Andy Zalkin",
        "team": "Baby Sharks",
        "original_rank": 3,
        "adjusted_rank": 1.3,
        "total_frames_won": 21,
        "total_frames_lost": 28,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 2,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Arpan Patel",
        "team": "Baby Sharks",
        "original_rank": 5,
        "adjusted_rank": 4.8,
        "total_frames_won": 31,
        "total_frames_lost": 36,
        "total_matches_won": 3,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 14
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 2
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Erik Ljungberg",
        "team": "Baby Sharks",
        "original_rank": 5,
        "adjusted_rank": 7.0,
        "total_frames_won": 62,
        "total_frames_lost": 47,
        "total_matches_won": 10,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 4,
                "matches_lost": 1,
                "frames_won": 20,
                "frames_lost": 14
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 11
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 18,
                "frames_lost": 15
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Russell Wilcox",
        "team": "Baby Sharks",
        "original_rank": 7,
        "adjusted_rank": 8.9,
        "total_frames_won": 63,
        "total_frames_lost": 43,
        "total_matches_won": 7,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 5,
                "matches_lost": 0,
                "frames_won": 34,
                "frames_lost": 16
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 19,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Charish Patel",
        "team": "Shots!!!!",
        "original_rank": 7,
        "adjusted_rank": 6.4,
        "total_frames_won": 37,
        "total_frames_lost": 47,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 20,
                "frames_lost": 22
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ben Reid",
        "team": "Shots!!!!",
        "original_rank": 5,
        "adjusted_rank": 5.8,
        "total_frames_won": 26,
        "total_frames_lost": 19,
        "total_matches_won": 5,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 12,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Ben Boucher",
        "team": "Shots!!!!",
        "original_rank": 5,
        "adjusted_rank": 6.0,
        "total_frames_won": 44,
        "total_frames_lost": 36,
        "total_matches_won": 7,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 15,
                "frames_lost": 11
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Katrel Ortiz",
        "team": "Shots!!!!",
        "original_rank": 5,
        "adjusted_rank": 4.4,
        "total_frames_won": 22,
        "total_frames_lost": 31,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Marisa Woo",
        "team": "Shots!!!!",
        "original_rank": 3,
        "adjusted_rank": 2.3,
        "total_frames_won": 14,
        "total_frames_lost": 22,
        "total_matches_won": 1,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 4,
                "frames_won": 13,
                "frames_lost": 17
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Ed Reyes",
        "team": "Shots!!!!",
        "original_rank": 6,
        "adjusted_rank": 7.2,
        "total_frames_won": 42,
        "total_frames_lost": 35,
        "total_matches_won": 5,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 10
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 12
            }
        }
    },
    {
        "name": "Courtney Prescott",
        "team": "Shots!!!!",
        "original_rank": 5,
        "adjusted_rank": 4.4,
        "total_frames_won": 14,
        "total_frames_lost": 22,
        "total_matches_won": 2,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 8,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Cory Moelis",
        "team": "Shots!!!!",
        "original_rank": 6,
        "adjusted_rank": 7.0,
        "total_frames_won": 24,
        "total_frames_lost": 20,
        "total_matches_won": 3,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 16
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Alan Gil",
        "team": "Silent Predators",
        "original_rank": 7,
        "adjusted_rank": 10.3,
        "total_frames_won": 47,
        "total_frames_lost": 34,
        "total_matches_won": 7,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 18,
                "frames_lost": 13
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 13,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 10
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Corinne Chen",
        "team": "Silent Predators",
        "original_rank": 4,
        "adjusted_rank": 3.0,
        "total_frames_won": 39,
        "total_frames_lost": 38,
        "total_matches_won": 4,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 9,
                "frames_lost": 14
            },
            "5": {
                "rank": 5,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 18,
                "frames_lost": 11
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 12,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Wayne Chow",
        "team": "Silent Predators",
        "original_rank": 7,
        "adjusted_rank": 7.6,
        "total_frames_won": 51,
        "total_frames_lost": 66,
        "total_matches_won": 5,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 4,
                "frames_won": 31,
                "frames_lost": 38
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 11
            }
        }
    },
    {
        "name": "Thomas Shuler",
        "team": "Silent Predators",
        "original_rank": 7,
        "adjusted_rank": 7.4,
        "total_frames_won": 39,
        "total_frames_lost": 48,
        "total_matches_won": 3,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 18,
                "frames_lost": 22
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Garrett London",
        "team": "Silent Predators",
        "original_rank": 6,
        "adjusted_rank": 5.8,
        "total_frames_won": 10,
        "total_frames_lost": 12,
        "total_matches_won": 1,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Safwan Saif",
        "team": "Silent Predators",
        "original_rank": 7,
        "adjusted_rank": 12.4,
        "total_frames_won": 65,
        "total_frames_lost": 27,
        "total_matches_won": 9,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 4,
                "matches_lost": 1,
                "frames_won": 32,
                "frames_lost": 18
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 14,
                "frames_lost": 1
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 1
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            }
        }
    },
    {
        "name": "Pavi Vetriselvan",
        "team": "Alpha Sheep",
        "original_rank": 5,
        "adjusted_rank": 5.5,
        "total_frames_won": 53,
        "total_frames_lost": 43,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 15
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 13,
                "frames_lost": 12
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 1
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Stephanie Tortora",
        "team": "Alpha Sheep",
        "original_rank": 3,
        "adjusted_rank": 3.0,
        "total_frames_won": 29,
        "total_frames_lost": 24,
        "total_matches_won": 6,
        "total_matches_lost": 3,
        "oponent_breakdown": {
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 10,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 3,
                "matches_lost": 0,
                "frames_won": 12,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 0
            }
        }
    },
    {
        "name": "Patrick Freed",
        "team": "Alpha Sheep",
        "original_rank": 6,
        "adjusted_rank": 5.7,
        "total_frames_won": 32,
        "total_frames_lost": 43,
        "total_matches_won": 1,
        "total_matches_lost": 7,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 14
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 5
            },
            "2": {
                "rank": 2,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Nick Palmer",
        "team": "Alpha Sheep",
        "original_rank": 5,
        "adjusted_rank": 4.5,
        "total_frames_won": 25,
        "total_frames_lost": 29,
        "total_matches_won": 3,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 6
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 7
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 7,
                "frames_lost": 12
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Mathew Chiaravalloti",
        "team": "Alpha Sheep",
        "original_rank": 5,
        "adjusted_rank": 3.7,
        "total_frames_won": 21,
        "total_frames_lost": 36,
        "total_matches_won": 3,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 8,
                "frames_lost": 6
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 2,
                "frames_lost": 10
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 4,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "John Giordano",
        "team": "Alpha Sheep",
        "original_rank": 6,
        "adjusted_rank": 6.5,
        "total_frames_won": 56,
        "total_frames_lost": 54,
        "total_matches_won": 8,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 8
            },
            "6": {
                "rank": 6,
                "matches_won": 3,
                "matches_lost": 2,
                "frames_won": 22,
                "frames_lost": 24
            },
            "7": {
                "rank": 7,
                "matches_won": 4,
                "matches_lost": 0,
                "frames_won": 24,
                "frames_lost": 16
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Osmar Olivo",
        "team": "The Ballers",
        "original_rank": 5,
        "adjusted_rank": 4.7,
        "total_frames_won": 14,
        "total_frames_lost": 17,
        "total_matches_won": 2,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 3
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Kirby Kohlmorgen",
        "team": "The Ballers",
        "original_rank": 5,
        "adjusted_rank": 3.7,
        "total_frames_won": 23,
        "total_frames_lost": 37,
        "total_matches_won": 2,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 11,
                "frames_lost": 12
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 10,
                "frames_lost": 18
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Colby Tresness",
        "team": "The Ballers",
        "original_rank": 6,
        "adjusted_rank": 7.8,
        "total_frames_won": 52,
        "total_frames_lost": 48,
        "total_matches_won": 7,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 14,
                "frames_lost": 24
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 9
            },
            "6": {
                "rank": 6,
                "matches_won": 4,
                "matches_lost": 0,
                "frames_won": 24,
                "frames_lost": 12
            },
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Jerzy Fischer",
        "team": "The Ballers",
        "original_rank": 6,
        "adjusted_rank": 7.0,
        "total_frames_won": 20,
        "total_frames_lost": 15,
        "total_matches_won": 2,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 7,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 8,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Andreas Nilsson",
        "team": "The Ballers",
        "original_rank": 7,
        "adjusted_rank": 9.4,
        "total_frames_won": 55,
        "total_frames_lost": 48,
        "total_matches_won": 6,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 2
            },
            "5": {
                "rank": 5,
                "matches_won": 4,
                "matches_lost": 1,
                "frames_won": 32,
                "frames_lost": 20
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 8
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "9": {
                "rank": 9,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Nick Demarco",
        "team": "The Ballers",
        "original_rank": 5,
        "adjusted_rank": 5.8,
        "total_frames_won": 28,
        "total_frames_lost": 20,
        "total_matches_won": 4,
        "total_matches_lost": 2,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 9,
                "frames_lost": 3
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 2
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Kirby Kohlmorgen (Forfeit)",
        "team": "The Ballers",
        "original_rank": 5,
        "adjusted_rank": 4.5,
        "total_frames_won": 0,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Kym Ganade",
        "team": "The Ballers",
        "original_rank": 6,
        "adjusted_rank": 3.9,
        "total_frames_won": 34,
        "total_frames_lost": 64,
        "total_matches_won": 3,
        "total_matches_lost": 8,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 23
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 8,
                "frames_lost": 28
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 5,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Ed Tesler",
        "team": "Pool Beings",
        "original_rank": 5,
        "adjusted_rank": 2.0,
        "total_frames_won": 40,
        "total_frames_lost": 63,
        "total_matches_won": 2,
        "total_matches_lost": 10,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 4,
                "frames_won": 8,
                "frames_lost": 19
            },
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 24,
                "frames_lost": 22
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 2,
                "frames_lost": 10
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 7
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Dominic Cashiola",
        "team": "Pool Beings",
        "original_rank": 4,
        "adjusted_rank": 1.4,
        "total_frames_won": 8,
        "total_frames_lost": 26,
        "total_matches_won": 0,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 2,
                "frames_lost": 15
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Frank Dutan",
        "team": "Pool Beings",
        "original_rank": 3,
        "adjusted_rank": 2.5,
        "total_frames_won": 35,
        "total_frames_lost": 26,
        "total_matches_won": 5,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 15,
                "frames_lost": 9
            },
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 14,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 3,
                "frames_lost": 2
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Camryn Lessing",
        "team": "Pool Beings",
        "original_rank": 3,
        "adjusted_rank": 0.8,
        "total_frames_won": 30,
        "total_frames_lost": 34,
        "total_matches_won": 4,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 2,
                "frames_won": 11,
                "frames_lost": 15
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 2,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 0,
                "frames_won": 10,
                "frames_lost": 6
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            }
        }
    },
    {
        "name": "Jonah Yang",
        "team": "Pool Beings",
        "original_rank": 3,
        "adjusted_rank": 0.2,
        "total_frames_won": 23,
        "total_frames_lost": 30,
        "total_matches_won": 4,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 6,
                "frames_lost": 8
            },
            "8": {
                "rank": 8,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 6,
                "frames_lost": 4
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 7,
                "frames_lost": 11
            },
            "7": {
                "rank": 7,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            }
        }
    },
    {
        "name": "Julia Goodkin",
        "team": "Pool Beings",
        "original_rank": 3,
        "adjusted_rank": 2.3,
        "total_frames_won": 22,
        "total_frames_lost": 22,
        "total_matches_won": 2,
        "total_matches_lost": 4,
        "oponent_breakdown": {
            "3": {
                "rank": 3,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 13,
                "frames_lost": 6
            },
            "8": {
                "rank": 8,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 7
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 9
            }
        }
    },
    {
        "name": "Christian Cashiola",
        "team": "Pool Beings",
        "original_rank": 4,
        "adjusted_rank": 2.7,
        "total_frames_won": 17,
        "total_frames_lost": 26,
        "total_matches_won": 0,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 5
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 5,
                "frames_lost": 10
            }
        }
    },
    {
        "name": "Brendan Geen",
        "team": "6 Guys 8 Balls",
        "original_rank": 3,
        "adjusted_rank": 1.1,
        "total_frames_won": 37,
        "total_frames_lost": 37,
        "total_matches_won": 5,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 12,
                "frames_lost": 7
            },
            "3": {
                "rank": 3,
                "matches_won": 1,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 12
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 3,
                "frames_lost": 9
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 9,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "Raj Narayan",
        "team": "6 Guys 8 Balls",
        "original_rank": 3,
        "adjusted_rank": -0.0,
        "total_frames_won": 6,
        "total_frames_lost": 31,
        "total_matches_won": 0,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 1,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 4,
                "frames_lost": 6
            }
        }
    },
    {
        "name": "David Panger",
        "team": "6 Guys 8 Balls",
        "original_rank": 4,
        "adjusted_rank": 1.8,
        "total_frames_won": 21,
        "total_frames_lost": 39,
        "total_matches_won": 3,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "4": {
                "rank": 4,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 11
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            },
            "5": {
                "rank": 5,
                "matches_won": 1,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 18
            },
            "2": {
                "rank": 2,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 0,
                "frames_lost": 5
            }
        }
    },
    {
        "name": "Miles Yaeger",
        "team": "6 Guys 8 Balls",
        "original_rank": 4,
        "adjusted_rank": 1.4,
        "total_frames_won": 20,
        "total_frames_lost": 43,
        "total_matches_won": 3,
        "total_matches_lost": 6,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 2,
                "matches_lost": 3,
                "frames_won": 10,
                "frames_lost": 20
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            },
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 3,
                "frames_won": 6,
                "frames_lost": 20
            }
        }
    },
    {
        "name": "Bradley Robertson",
        "team": "6 Guys 8 Balls",
        "original_rank": 6,
        "adjusted_rank": 6.2,
        "total_frames_won": 47,
        "total_frames_lost": 49,
        "total_matches_won": 5,
        "total_matches_lost": 5,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 16,
                "frames_lost": 16
            },
            "7": {
                "rank": 7,
                "matches_won": 2,
                "matches_lost": 1,
                "frames_won": 15,
                "frames_lost": 13
            },
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 9,
                "frames_lost": 13
            },
            "3": {
                "rank": 3,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 3,
                "frames_lost": 4
            },
            "4": {
                "rank": 4,
                "matches_won": 1,
                "matches_lost": 0,
                "frames_won": 4,
                "frames_lost": 3
            }
        }
    },
    {
        "name": "Alden Gonzalez",
        "team": "6 Guys 8 Balls",
        "original_rank": 5,
        "adjusted_rank": 2.4,
        "total_frames_won": 27,
        "total_frames_lost": 51,
        "total_matches_won": 1,
        "total_matches_lost": 9,
        "oponent_breakdown": {
            "5": {
                "rank": 5,
                "matches_won": 0,
                "matches_lost": 5,
                "frames_won": 12,
                "frames_lost": 22
            },
            "4": {
                "rank": 4,
                "matches_won": 0,
                "matches_lost": 2,
                "frames_won": 0,
                "frames_lost": 10
            },
            "7": {
                "rank": 7,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 5,
                "frames_lost": 6
            },
            "6": {
                "rank": 6,
                "matches_won": 1,
                "matches_lost": 1,
                "frames_won": 10,
                "frames_lost": 13
            }
        }
    },
    {
        "name": "Chad Charrette",
        "team": "6 Guys 8 Balls",
        "original_rank": 3,
        "adjusted_rank": 2.3,
        "total_frames_won": 1,
        "total_frames_lost": 5,
        "total_matches_won": 0,
        "total_matches_lost": 1,
        "oponent_breakdown": {
            "6": {
                "rank": 6,
                "matches_won": 0,
                "matches_lost": 1,
                "frames_won": 1,
                "frames_lost": 5
            }
        }
    }
]
```
