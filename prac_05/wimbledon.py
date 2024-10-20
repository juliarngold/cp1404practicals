def main():
    player_to_wins = {}
    winner_countries = set()
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        print("Wimbledon Champions:")
        fill_set_and_dict(in_file, player_to_wins, winner_countries)
        print_players(player_to_wins)
        winner_countries = sorted(winner_countries)
        print_results(winner_countries)


def print_results(winner_countries):
    """Print list countries winners"""
    print(f"\nThese {len(winner_countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in winner_countries))


def print_players(player_to_wins):
    """Print players and their win count"""
    for player in player_to_wins:
        print(f"{player} {player_to_wins[player]}")


def fill_set_and_dict(in_file, player_to_wins, winner_countries):
    """Put players and countries from line to winner_countries set and player_to_wins dictionary"""
    for line in in_file:
        line = line.split(',')
        winner_countries.add(line[1])
        if line[2] in player_to_wins:
            player_to_wins[line[2]] = player_to_wins[line[2]] + 1
        else:
            player_to_wins[line[2]] = 1


main()