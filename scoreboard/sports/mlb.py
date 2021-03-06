import datetime
import json
from ..utils import get_game_data, get_live_content

BASE_URL = 'https://statsapi.mlb.com/api/v1/'

GAMES_URL = BASE_URL + 'schedule?sportId=1&startDate={0}&endDate={0}'
LIVE_CONTENT_URL = BASE_URL + 'game/{0}/content'


def get_live_scoreboard(game_date, status='Live'):
    """
    return list
    """
    return get_game_data(GAMES_URL.format(game_date.strftime('%Y-%m-%d')), status)


def get_live_image(game_id):
    """
    return dict
    """
    return get_live_content(LIVE_CONTENT_URL.format(str(game_id)))
