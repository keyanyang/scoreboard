from scoreboard.sports import mlb
import datetime
import sys
import time
from scoreboard.utils import display
import curses

today = datetime.datetime.today()
#samples = [['Los Angeles Dodgers', '7', 'Arizona Diamondbacks', '3'], ['Texas Rangers', '4', 'Los Angeles Angels', '4'], ['Oakland Athletics', '7', 'Seattle Mariners', '3']]


def mlb_live(window):
    while 1:
        mlb_live_games = mlb.get_live_scoreboard(today)
        if not mlb_live_games:
            window.addstr("No game in progress")
            window.refresh()
            time.sleep(3)
            return
        window.erase()
        window.addstr(display(mlb_live_games))
        window.refresh()
        time.sleep(20)


def main():
    curses.wrapper(mlb_live)


if __name__ == '__main__':
    main()
