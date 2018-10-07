import argparse
from scoreboard.sports import mlb, nhl, nfl
import datetime
import sys
import os
import time
from scoreboard.table import display_table
from scoreboard.img_convert import draw
import colorama
import requests
from collections import deque

today = datetime.datetime.today()


def put_cursor(x,y):
    print("\x1b[{};{}H".format(y+1,x+1))


def clear():
    print("\x1b[2J")


def mlb_live():
    colorama.init()
    clear()
    while 1:
        now = datetime.datetime.now().strftime("%I:%M %p")
        # games table
        lives_games = mlb.get_live_scoreboard(today)
        put_cursor(0,0)
        print(" MLB ⚾    {}\n".format(now) + display_table(lives_games))
        print("\n")

        if not lives_games:
            print("No game in progress. Existing now.")
            time.sleep(15)
            return


def nhl_live():
    colorama.init()
    clear()
    while 1:
        now = datetime.datetime.now().strftime("%I:%M %p")
        lives_games = nhl.get_live_scoreboard(today)
        put_cursor(0,0)
        print(" NHL 🏒    {}\n".format(now) + display_table(lives_games))
        print("\n")

        if not lives_games:
            print("No game in progress. Existing now.")
            time.sleep(15)
            return


def nfl_live():
    colorama.init()
    clear()
    while 1:
        now = datetime.datetime.now().strftime("%I:%M %p")
        lives_games = nfl.get_live_scoreboard()
        put_cursor(0,0)
        print(" NFL 🏈    {}\n".format(now) + display_table(lives_games, id=False))
        print("\n")

        if not lives_games:
            print("No game in progress. Existing now.")
            time.sleep(15)
            return


def all_live():
    colorama.init()
    clear()
    while 1:
        try:
            now = datetime.datetime.now().strftime("%I:%M %p")
            mlb_live_games, nhl_live_games, nfl_lives_games = mlb.get_live_scoreboard(today), nhl.get_live_scoreboard(today), nfl.get_live_scoreboard()
            put_cursor(0,0)
            print(now + "\n")
            print(" MLB ⚾\n" + display_table(mlb_live_games))
            print("\n\n")
            print(" NHL 🏒\n" + display_table(nhl_live_games))
            print("\n\n")
            print(" NFL 🏈\n" + display_table(nfl_lives_games, id=False))
            print("\n\n")
            print("Control + c to exit")
            if not [mlb_live_games, nhl_live_games, nfl_lives_games]:
                print("No game in progress. Existing now.")
                time.sleep(5)
                return
        except KeyboardInterrupt:
            print("Existing now")
            time.sleep(0.5)
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mlb', action='store_true', help='MLB live')
    parser.add_argument('--nhl', action='store_true', help='NHL live')
    parser.add_argument('--nfl', action='store_true', help='NFL live')
    args = parser.parse_args()
    if args.mlb:
        mlb_live()
    elif args.nhl:
        nhl_live()
    elif args.nfl:
        nfl_live()
    else:
        all_live()


if __name__ == '__main__':
    main()