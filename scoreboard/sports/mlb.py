import datetime
import json
from ..utils import get_data

BASE_URL = 'https://statsapi.mlb.com/api/v1/'
GAMES_URL = BASE_URL + 'schedule?sportId=1&startDate={0}&endDate={0}'


def get_live_scoreboard(game_date):
    """
    return list
    """
    return get_data(GAMES_URL.format(game_date.strftime('%Y-%m-%d')), 'Live')
