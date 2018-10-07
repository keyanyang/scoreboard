import datetime
import json
from ..utils import get_nfl_game_data

BASE_URL = 'http://www.nfl.com/'

GAMES_URL = BASE_URL + 'liveupdate/scorestrip/ss.xml'


def get_live_scoreboard():
    """
    return list
    """
    return get_nfl_game_data(GAMES_URL)
