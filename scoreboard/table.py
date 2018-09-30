from tabulate import tabulate


def display_table(games):
    games_without_id = [g[1:] for g in games]
    return tabulate(games_without_id, headers=['away', '', 'home', ''], tablefmt="fancy_grid")
