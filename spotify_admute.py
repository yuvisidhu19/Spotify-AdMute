import spotipy, pyautogui
import time, psutil
import spotipy.util as util
import os
from dotenv import load_dotenv

load_dotenv()

#input your spotify credentials here (Available at https://developer.spotify.com/dashboard/login):
cid = os.getenv('cid')
secret = os.getenv('secret')
username = os.getenv('name')

#Authorization (our browser will pop-up for a second)
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback"
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

flag = True
while "Spotify.exe" in (i.name() for i in psutil.process_iter()):   #code will stop running after you exit spotify
    time.sleep(0.5)   #checks for ad every 0.5 seconds
    try:
        if sp.current_user_playing_track()['currently_playing_type'] == 'ad' and flag:
            flag = False
            pyautogui.press('volumemute')
        elif sp.current_user_playing_track()['currently_playing_type'] != 'ad' and not flag:
            flag = True
            pyautogui.press('volumemute')
    except:
        pass
