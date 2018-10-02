import pytest
import datetime
from scoreboard.sports import mlb


@pytest.fixture()
def example_game_date():
    return datetime.datetime.strptime('9/15/2018', '%m/%d/%Y')


def test_get_live_scoreboard(example_game_date):
    expected = [[531624, 'Los Angeles Dodgers', '17', 'St. Louis Cardinals', '4'], 
                [531633, 'Washington Nationals', '7', 'Atlanta Braves', '1'], 
                [531623, 'Detroit Tigers', '0', 'Cleveland Indians', '15'], 
                [531621, 'Cincinnati Reds', '0', 'Chicago Cubs', '1'], 
                [531627, 'New York Mets', '3', 'Boston Red Sox', '5'], 
                [531632, 'Toronto Blue Jays', '8', 'New York Yankees', '7'], 
                [531628, 'Oakland Athletics', '5', 'Tampa Bay Rays', '7'], 
                [531620, 'Chicago White Sox', '2', 'Baltimore Orioles', '0'], 
                [531625, 'Miami Marlins', '4', 'Philadelphia Phillies', '5'], 
                [531619, 'Arizona Diamondbacks', '4', 'Houston Astros', '10'], 
                [531629, 'Pittsburgh Pirates', '3', 'Milwaukee Brewers', '1'], 
                [531626, 'Minnesota Twins', '3', 'Kansas City Royals', '10'], 
                [531631, 'Texas Rangers', '6', 'San Diego Padres', '3'], 
                [531622, 'Colorado Rockies', '0', 'San Francisco Giants', '3'], 
                [531630, 'Seattle Mariners', '6', 'Los Angeles Angels', '5']]
    actual = mlb.get_live_scoreboard(example_game_date, 'Final')
    assert expected == actual


@pytest.fixture()
def example_game_id():
    return 531630


def test_get_live_image(example_game_id):
    expected = {'media_id': '2490596383', 'kicker': 'CG: SEA@LAA - 9/15/18', 'description': 'Condensed Game: SEA@LAA - 9/15/18', 'img_url': 'https://mediadownloads.mlb.com/mlbam/2018/09/16/images/mlbf_2490596383_th_43.jpg'}
    actual = mlb.get_live_image(example_game_id)
    assert expected == actual
