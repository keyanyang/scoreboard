"""Scoreboard utils and helpers."""
from __future__ import division

import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import time
import json


def _get_url(url):
    response = requests.Session()
    retries = Retry(total=10, backoff_factor=.1)
    response.mount('http://', HTTPAdapter(max_retries=retries))
    response = response.get(url, timeout=5)
    response.raise_for_status()
    return response


def _convert_schedule_json(data_json, game_state):
    """
    return list
    """
    games_list = []
    for day in data_json['dates']:
        for game in day['games']:
            if game['status']['abstractGameState'] == game_state:
                games_list.append([game['gamePk'],
                                   game['teams']['away']['team']['name'],
                                   str(game['teams']['away']['score']),
                                   game['teams']['home']['team']['name'],
                                   str(game['teams']['home']['score'])
                                  ])
    return games_list


def get_game_data(url, game_state):
    """
    return list
    """
    response = _get_url(url)
    return _convert_schedule_json(json.loads(response.text), game_state)


def _convert_content_json(data_json):
    """
    return dict
    """
    live_content = {}
    items = data_json['highlights']['live']['items']
    if not items:
        return {}
    else:
        last_item = items[-1]
        live_content['media_id'] = last_item['id']
        live_content['kicker'] = last_item['kicker']
        live_content['description'] = last_item['description']

        for cut in last_item['image']['cuts']:
            if cut['width'] >= 400 and cut['width'] <= 750 and cut['height'] >= 300 and cut['height']<=440:
                live_content['img_url'] = cut['src']
                return live_content
        return {}


def get_live_content(url):
    """
    return list
    """
    response = _get_url(url)
    return _convert_content_json(json.loads(response.text))


def _convert_live_json(data_json):
    """
    return dict
    """
    return data_json['liveData']['play']['currentPlay']['result']['description']


def get_current_play(url):
    """
    return str
    """
    response = _get_url(url)
    return _convert_live_json(json.loads(response.text))
