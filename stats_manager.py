import os
from datetime import datetime

STATS_FILE = "tictactoe_stats.txt"


def write_stat(winner, player_symbols):
    """Append a new game statistic record to the text file."""

    write_headers = not os.path.exists(STATS_FILE)

    with open(STATS_FILE, "a") as file:
        if write_headers:
            file.write("game_id,winner,player_symbols,num_moves,game_date\n")

        game_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game_id = sum(1 for line in open(STATS_FILE))
        file.write(f"{game_id},{winner},{player_symbols},{game_date}\n")


def read_stats():
    """Read and print all game statistics from the text file."""
    try:
        with open(STATS_FILE, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Statistics file does not exist yet.")
