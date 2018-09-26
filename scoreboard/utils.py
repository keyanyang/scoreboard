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


def _convert_live_json(data_json, game_state):
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
    return _convert_live_json(json.loads(response.text), game_state)


def display(games_list):
    text_display = ""
    for g in games_list:
        text_display += g[0] + ' (' + g[1] + ') at ' + g[2] + ' (' + g[3] + ')\n'
    return text_display


def _convert_content_json(data_json):
    """
    return dict
    """
    live_content = {}
    last_item = data_json['highlights']['live']['items'][-1]
    live_content['description'] = last_item['description']
    live_content['img_url'] = last_item['image']['cuts'][-1]['src']
    return live_content


def get_live_content(url):
    """
    return list
    """
    response = _get_url(url)
    return _convert_content_json(json.loads(response.text))
