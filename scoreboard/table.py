from tabulate import tabulate
from colorclass import Color


team_color = {
    # MLB
    "Oakland Athletics": Color('{bggreen}{hiyellow}Oakland Athletics{/hiyellow}{/bggreen}'),
    "Pittsburgh Pirates": Color('{hibgyellow}{black}Pittsburgh Pirates{/black}{/hibgyellow}'),
    "San Diego Padres": Color('{bgblack}{hiblue}San Diego Padres{/hiblue}{/bgblack}'),
    "Seattle Mariners": Color('{hibggreen}{black}Seattle Mariners{/black}{/hibggreen}'),

    "San Francisco Giants": Color('{bgyellow}{black}San Francisco Giants{/black}{/bgyellow}'),
    "St. Louis Cardinals": Color('{hibgred}{black}St. Louis Cardinals{/black}{/hibgred}'),
    "Tampa Bay Rays": Color('{bgblue}{hiblue}Tampa Bay Rays{/bgblue}{/bgblack}'),
    "Texas Rangers": Color('{bgblue}{hired}Texas Rangers{/hired}{/bgblue}'),

    "Toronto Blue Jays": Color('{hibgblue}{black}Toronto Blue Jays{/black}{/hibgblue}'),
    "Minnesota Twins": Color('{hibgblue}{hired}Minnesota Twins{/hired}{/hibgblue}'),
    "Philadelphia Phillies": Color('{hibgwhite}{hired}Philadelphia Phillies{/hired}{/hibgwhite}'),
    "Atlanta Braves": Color('{bgred}{white}Atlanta Braves{/white}{/bgred}'),

    "Chicago White Sox": Color('{hibgblack}{hiwhite}Chicago White Sox{/hiwhite}{/hibgblack}'),
    "Miami Marlins": Color('{hibggreen}{black}Miami Marlins{/black}{/hibggreen}'),
    "New York Yankees": Color('{bgwhite}{black}New York Yankees{/black}{/bgwhite}'),
    "Milwaukee Brewers": Color('{bgblue}{hiyellow}Milwaukee Brewers{/hiyellow}{/bgblue}'),

    "Los Angeles Angels": Color('{bgred}{hiblue}Los Angeles Angels{/hiblue}{/bgred}'),
    "Arizona Diamondbacks": Color('{bgred}{black}Arizona Diamondbacks{/black}{/bgred}'),
    "Baltimore Orioles": Color('{bgyellow}{white}Baltimore Orioles{/white}{/bgyellow}'),
    "Boston Red Sox": Color('{bgwhite}{hired}Boston Red Sox{/hired}{/bgwhite}'),

    "Chicago Cubs": Color('{hibgblue}{hired}Chicago Cubs{/hired}{/hibgblue}'),
    "Cincinnati Reds": Color('{hibgwhite}{red}Cincinnati Reds{/red}{/hibgwhite}'),
    "Cleveland Indians": Color('{bgblue}{hired}Cleveland Indians{/hired}{/bgblue}'),
    "Colorado Rockies": Color('{hibgwhite}{magenta}Colorado Rockies{/magenta}{/hibgwhite}'),

    "Detroit Tigers": Color('{hibgwhite}{blue}Detroit Tigers{/blue}{/hibgwhite}'),
    "Houston Astros": Color('{bgyellow}{blue}Houston Astros{/blue}{/bgyellow}'),
    "Kansas City Royals": Color('{bgwhite}{blue}Kansas City Royals{/blue}{/bgwhite}'),
    "Los Angeles Dodgers": Color('{hibgblue}{hiwhite}Los Angeles Dodgers{/hiwhite}{/hibgblue}'),

    "Washington Nationals": Color('{bgwhite}{hired}Washington Nationals{/hired}{/bgwhite}'),
    "New York Mets": Color('{hibgblue}{yellow}New York Mets{/yellow}{/hibgblue}'),


    # NHL
    "Boston Bruins": Color('{bggreen}{hiyellow}Boston Bruins{/hiyellow}{/bggreen}'),
    "Buffalo Sabres": Color('{hibgyellow}{black}Buffalo Sabres{/black}{/hibgyellow}'),
    "Detroit Red Wings": Color('{bgblack}{hiblue}Detroit Red Wings{/hiblue}{/bgblack}'),
    "Florida Panthers": Color('{hibggreen}{black}Florida Panthers{/black}{/hibggreen}'),

    "Montreal Canadiens": Color('{bgyellow}{black}Montreal Canadiens{/black}{/bgyellow}'),
    "Ottawa Senators": Color('{hibgred}{black}Ottawa Senators{/black}{/hibgred}'),
    "Tampa Bay Lightning": Color('{bgblue}{hiblue}Tampa Bay Lightning{/bgblue}{/bgblack}'),
    "Toronto Maple Leafs": Color('{bgblue}{hired}Toronto Maple Leafs{/hired}{/bgblue}'),

    "Carolina Hurricanes": Color('{hibgred}{black}Carolina Hurricanes{/black}{/hibgred}'), #
    "Columbus Blue Jackets": Color('{hibgblue}{hired}Columbus Blue Jackets{/hired}{/hibgblue}'),
    "New Jersey Devils": Color('{hibgwhite}{hired}New Jersey Devils{/hired}{/hibgwhite}'),
    "New York Islanders": Color('{bgred}{white}New York Islanders{/white}{/bgred}'),

    "New York Rangers": Color('{hibgblue}{hired}New York Rangers{/hired}{/hibgblue}'), #
    "Philadelphia Flyers": Color('{hibggreen}{black}Philadelphia Flyers{/black}{/hibggreen}'),
    "Pittsburgh Penguins": Color('{bgwhite}{black}Pittsburgh Penguins{/black}{/bgwhite}'),
    "Washington Capitals": Color('{bgblue}{hiyellow}Washington Capitals{/hiyellow}{/bgblue}'),

    "Chicago Blackhawks": Color('{bgred}{hiblue}Chicago Blackhawks{/hiblue}{/bgred}'),
    "Colorado Avalanche": Color('{bgred}{black}Colorado Avalanche{/black}{/bgred}'),
    "Dallas Stars": Color('{bgyellow}{white}Dallas Stars{/white}{/bgyellow}'),
    "Minnesota Wild": Color('{bgwhite}{hired}Minnesota Wild{/hired}{/bgwhite}'),

    "Nashville Predators": Color('{hibgblue}{hired}Nashville Predators{/hired}{/hibgblue}'),
    "St. Louis Blues": Color('{hibgwhite}{red}St. Louis Blues{/red}{/hibgwhite}'),
    "Winnipeg Jets": Color('{bgblue}{hired}Winnipeg Jets{/hired}{/bgblue}'),
    "Anaheim Ducks": Color('{hibgwhite}{magenta}Anaheim Ducks{/magenta}{/hibgwhite}'),

    "Arizona Coyotes": Color('{hibgwhite}{blue}Arizona Coyotes{/blue}{/hibgwhite}'),
    "Calgary Flames": Color('{bgyellow}{blue}Calgary Flames{/blue}{/bgyellow}'),
    "Edmonton Oilers": Color('{bgwhite}{blue}Edmonton Oilers{/blue}{/bgwhite}'),
    "Los Angeles Kings": Color('{hibgblue}{hiwhite}Los Angeles Kings{/hiwhite}{/hibgblue}'),

    "San Jose Sharks": Color('{bgwhite}{hired}San Jose Sharks{/hired}{/bgwhite}'),
    "Vancouver Canucks": Color('{hibgblue}{yellow}Vancouver Canucks{/yellow}{/hibgblue}'),
    "Vegas Golden Knights": Color('{hibgblue}{yellow}Vegas Golden Knights{/yellow}{/hibgblue}'),

    # NFL
    'PHI': Color('{bggreen}{hiwhite}PHI 🦅  {/hiwhite}{/bggreen}'),
    'ATL': ':diamonds: ATL',
    'BAL': 'BAL',
    'BUF': 'BUF',
    'CLE': 'CLE',
    'PIT': 'PIT',
    'IND': 'IND',
    'CIN': 'CIN',
    'MIA': ':dolphin: MIA',
    'TEN': 'TEN',
    'MIN': Color('{hibgwhite}{yellow}MIN 😈  {/yellow}{/hibgwhite}'),
    'SF': Color('{bgwhite}{hired}SF 🧔  {/hired}{/bgwhite}'),
    'NE': 'NE',
    'HOU': 'HOU',
    'NO': 'NO',
    'TB': ':skull_and_crossbones: TB',
    'NYG': 'NYG',
    'JAX': 'JAX',
    'LAC': Color('{bgblue}{hiyellow}LAC ⚡  {/hiyellow}{/bgblue}'),
    'KC': 'KC',
    'ARI': Color('{hibgred}{black}ARI 🐤  {/black}{/hibgred}'),
    'WAS': ':bird: WAS',
    'CAR': 'CAR',
    'DAL': 'DAL',
    'DEN': 'DEN',
    'SEA': Color('{bgblue}{higreen}LAC 🦅  {/higreen}{/bgblue}'),
    'GB': 'GB',
    'CHI': 'CHI',
    'DET': ':lion_face: DET',
    'NYJ': 'NYJ',
    'OAK': Color('{bgblack}{hiwhite}OAK ☠  {/hiwhite}{/bgblack}'),
    'LA': Color('{bgblue}{yellow}LA 🐏  {/yellow}{/bgblue}')
}


def _colorize_team_name(games):
    for game in games:
        game[0] = team_color.get(game[0], game[0])
        game[2] = team_color.get(game[2], game[2])
    return games


def display_table(games, id=True, color=True):
    if id:
        games_without_id = [g[1:] for g in games]
    else:
        games_without_id = games

    if color:
        games_without_id = _colorize_team_name(games_without_id)
    return tabulate(games_without_id, headers=['away', '', 'home', ''], tablefmt="fancy_grid")
