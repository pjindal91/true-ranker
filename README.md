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
