from tabulate import tabulate
from colorclass import Color


team_color = {
    "Oakland Athletics": Color('{bggreen}{hiyellow}Oakland Athletics{/hiyellow}{/bggreen}'), #
    "Pittsburgh Pirates": Color('{hibgyellow}{black}Pittsburgh Pirates{/black}{/hibgyellow}'), #
    "San Diego Padres": Color('{bgblack}{hiblue}San Diego Padres{/hiblue}{/bgblack}'), # 
    "Seattle Mariners": Color('{hibggreen}{black}Seattle Mariners{/black}{/hibggreen}'), #

    "San Francisco Giants": Color('{bgyellow}{black}San Francisco Giants{/black}{/bgyellow}'), #
    "St. Louis Cardinals": Color('{hibgred}{black}St. Louis Cardinals{/black}{/hibgred}'), #
    "Tampa Bay Rays": Color('{bgblue}{hiblue}Tampa Bay Rays{/bgblue}{/bgblack}'), #
    "Texas Rangers": Color('{bgblue}{hired}Texas Rangers{/hired}{/bgblue}'), #

    "Toronto Blue Jays": Color('{hibgblue}{black}Toronto Blue Jays{/black}{/hibgblue}'), #
    "Minnesota Twins": Color('{hibgblue}{hired}Minnesota Twins{/hired}{/hibgblue}'), #
    "Philadelphia Phillies": Color('{hibgwhite}{hired}Philadelphia Phillies{/hired}{/hibgwhite}'), #
    "Atlanta Braves": Color('{bgred}{white}Atlanta Braves{/white}{/bgred}'), #

    "Chicago White Sox": Color('{hibgblack}{hiwhite}Chicago White Sox{/hiwhite}{/hibgblack}'), #
    "Miami Marlins": Color('{hibggreen}{black}Miami Marlins{/black}{/hibggreen}'), #
    "New York Yankees": Color('{bgwhite}{black}New York Yankees{/black}{/bgwhite}'), #
    "Milwaukee Brewers": Color('{bgblue}{hiyellow}Milwaukee Brewers{/hiyellow}{/bgblue}'), #

    "Los Angeles Angels": Color('{bgred}{hiblue}Los Angeles Angels{/hiblue}{/bgred}'), #
    "Arizona Diamondbacks": Color('{bgred}{black}Arizona Diamondbacks{/black}{/bgred}'), # 
    "Baltimore Orioles": Color('{bgyellow}{white}Baltimore Orioles{/white}{/bgyellow}'), # 
    "Boston Red Sox": Color('{bgwhite}{hired}Boston Red Sox{/hired}{/bgwhite}'), #

    "Chicago Cubs": Color('{hibgblue}{hired}Chicago Cubs{/hired}{/hibgblue}'),
    "Cincinnati Reds": Color('{hibgwhite}{red}Cincinnati Reds{/red}{/hibgwhite}'),
    "Cleveland Indians": Color('{bgblue}{hired}Cleveland Indians{/hired}{/bgblue}'),
    "Colorado Rockies": Color('{hibgwhite}{magenta}Colorado Rockies{/magenta}{/hibgwhite}'),

    "Detroit Tigers": Color('{hibgwhite}{blue}Detroit Tigers{/blue}{/hibgwhite}'),
    "Houston Astros": Color('{bgyellow}{blue}Houston Astros{/blue}{/bgyellow}'),
    "Kansas City Royals": Color('{bgwhite}{blue}Kansas City Royals{/blue}{/bgwhite}'),
    "Los Angeles Dodgers": Color('{hibgblue}{hiwhite}Los Angeles Dodgers{/hiwhite}{/hibgblue}'),

    "Washington Nationals": Color('{bgwhite}{hired}Washington Nationals{/hired}{/bgwhite}'),
    "New York Mets": Color('{hibgblue}{yellow}New York Mets{/yellow}{/hibgblue}')
}

def colorize_team_name(games):
    for game in games:
        game[0] = team_color.get(game[0], game[0])
        game[2] = team_color.get(game[2], game[2])
    return games


def display_table(games):
    games_without_id = [g[1:] for g in games]
    games_without_id = colorize_team_name(games_without_id)
    return tabulate(games_without_id, headers=['away', '', 'home', ''], tablefmt="fancy_grid")
    