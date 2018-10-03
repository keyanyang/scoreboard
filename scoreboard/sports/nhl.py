import datetime
import json
from ..utils import get_game_data, get_live_content

BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'

GAMES_URL = BASE_URL + 'schedule?startDate={0}&endDate={0}'
LIVE_CONTENT_URL = BASE_URL + 'game/{0}/content'


def get_live_scoreboard(game_date):
    """
    return list
    """
    return get_game_data(GAMES_URL.format(game_date.strftime('%Y-%m-%d')), 'Live')


def get_live_image(game_id):
    """
    return dict
    """
    return get_live_content(LIVE_CONTENT_URL.format(str(game_id)))
