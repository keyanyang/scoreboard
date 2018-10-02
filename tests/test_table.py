import pytest
from scoreboard import table


@pytest.fixture()
def example_games():
    return [[531771, 'Oakland Athletics', '2', 'Pittsburgh Pirates', '1'], 
            [531775, 'San Diego Padres', '3', 'Seattle Mariners', '1'],

            [531775, 'San Francisco Giants', '3', 'St. Louis Cardinals', '1'],
            [531775, 'Tampa Bay Rays', '3', 'Texas Rangers', '1'],

            [531771, 'Toronto Blue Jays', '2', 'Minnesota Twins', '1'], 
            [531775, 'Philadelphia Phillies', '3', 'Atlanta Braves', '1'],

            [531771, 'Chicago White Sox', '2', 'Miami Marlins', '1'], 
            [531775, 'New York Yankees', '3', 'Milwaukee Brewers', '1'],

            [531771, 'Los Angeles Angels', '2', 'Arizona Diamondbacks', '1'],
            [531775, 'Baltimore Orioles', '3', 'Boston Red Sox', '1'],

            [531771, 'Chicago Cubs', '2', 'Cincinnati Reds', '1'], 
            [531775, 'Cleveland Indians', '3', 'Colorado Rockies', '1'],

            [531771, 'Detroit Tigers', '2', 'Houston Astros', '1'], 
            [531775, 'Kansas City Royals', '3', 'Los Angeles Dodgers', '1'],

            [531775, 'Washington Nationals', '3', 'New York Mets', '1']]


def test_get_live_image(example_games):
    expected = """╒═══════════════════════╤════╤══════════════════════╤════╕
│ away                  │    │ home                 │    │
╞═══════════════════════╪════╪══════════════════════╪════╡
│ Oakland Athletics     │  2 │ Pittsburgh Pirates   │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ San Diego Padres      │  3 │ Seattle Mariners     │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ San Francisco Giants  │  3 │ St. Louis Cardinals  │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Tampa Bay Rays        │  3 │ Texas Rangers        │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Toronto Blue Jays     │  2 │ Minnesota Twins      │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Philadelphia Phillies │  3 │ Atlanta Braves       │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Chicago White Sox     │  2 │ Miami Marlins        │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ New York Yankees      │  3 │ Milwaukee Brewers    │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Los Angeles Angels    │  2 │ Arizona Diamondbacks │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Baltimore Orioles     │  3 │ Boston Red Sox       │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Chicago Cubs          │  2 │ Cincinnati Reds      │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Cleveland Indians     │  3 │ Colorado Rockies     │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Detroit Tigers        │  2 │ Houston Astros       │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Kansas City Royals    │  3 │ Los Angeles Dodgers  │  1 │
├───────────────────────┼────┼──────────────────────┼────┤
│ Washington Nationals  │  3 │ New York Mets        │  1 │
╘═══════════════════════╧════╧══════════════════════╧════╛"""
    actual = table.display_table(example_games, color=False)
    assert expected == actual
