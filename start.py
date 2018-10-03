import argparse
from scoreboard.sports import mlb, nhl
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


def download_img(description_img_url):
    """
    save image and return img file name
    """
    if not os.path.exists('./scoreboard/img_cache'):
        os.makedirs('./scoreboard/img_cache')

    try:
        response = requests.get(description_img_url['img_url'])
    except KeyError:
        pass
    if response.status_code == 200:
        with open('./scoreboard/img_cache/{}.jpg'.format(description_img_url['media_id']), 'wb') as f:
            f.write(response.content)
        return description_img_url['media_id']


def remove_images():
    if not os.path.isdir('./scoreboard/img_cache'):
        return
    file_list = os.listdir('./scoreboard/img_cache')
    for filename in file_list:
        os.remove('./scoreboard/img_cache/' + filename)


def mlb_live():
    colorama.init()
    remove_images()
    clear()
    current_live_ids = []
    used_img_ids = []
    img_flow = deque()
    current_img = "Loading..."
    elapsed_time = 99
    while 1:
        now = datetime.datetime.now().strftime("%I:%M %p")
        # games table
        lives_games = mlb.get_live_scoreboard(today)
        current_live_ids = [game[0] for game in lives_games]
        put_cursor(0,0)
        print("    ⚾    {}\n".format(now) + display_table(lives_games))
        print("\n")
        print(current_img)

        if elapsed_time > 60:
            for game_id in current_live_ids:
                description_img_url = mlb.get_live_image(game_id)
                if not description_img_url:
                    continue
                if description_img_url['media_id'] not in used_img_ids:
                    img_name = download_img(description_img_url)
                    used_img_ids.append(img_name)

                    img_flow.appendleft(description_img_url)

            if not img_flow:
                current_img = ''
            elif len(img_flow) == 1:
                current_img = draw(img_flow[0])
            else:
                current_img = draw(img_flow.pop())
            start_time = time.time()

        if not lives_games:
            print("No game in progress. Existing now.")
            time.sleep(3)
            return
        put_cursor(0,0)
        time.sleep(3)
        elapsed_time = int(time.time() - start_time)


def nhl_live():
    colorama.init()
    remove_images()
    clear()
    current_live_ids = []
    used_img_ids = []
    img_flow = deque()
    current_img = "Loading..."
    elapsed_time = 99
    while 1:
        now = datetime.datetime.now().strftime("%I:%M %p")
        # games table
        lives_games = nhl.get_live_scoreboard(today)
        current_live_ids = [game[0] for game in lives_games]
        put_cursor(0,0)
        print("    🏒    {}\n".format(now) + display_table(lives_games))
        print("\n")
        print(current_img)

        if elapsed_time > 60:
            for game_id in current_live_ids:
                description_img_url = nhl.get_live_image(game_id)
                if not description_img_url:
                    continue
                if description_img_url['media_id'] not in used_img_ids:
                    img_name = download_img(description_img_url)
                    used_img_ids.append(img_name)

                    img_flow.appendleft(description_img_url)

            if not img_flow:
                current_img = ''
            elif len(img_flow) == 1:
                current_img = draw(img_flow[0])
            else:
                current_img = draw(img_flow.pop())
            start_time = time.time()

        if not lives_games:
            print("No game in progress. Existing now.")
            time.sleep(3)
            return
        put_cursor(0,0)
        time.sleep(3)
        elapsed_time = int(time.time() - start_time)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mlb', action='store_true', help='MLB live')
    parser.add_argument('--nhl', action='store_true', help='NHL live')
    args = parser.parse_args()
    if args.mlb:
        mlb_live()
    elif args.nhl:
        nhl_live()
    else:
        print("Please add argument --mlb or --nhl")


if __name__ == '__main__':
    main()
