import pandas as pd
import setup_functions as setup
import create_playlist as create

url = "https://raw.githubusercontent.com/JenB-DS/playlist_create/main/spotify_songs.csv"
music = pd.read_csv(url)

# how many songs inc. in the example (approx 3 mins)
cond = (music['duration_ms'] >= 160000) & (music['duration_ms'] <= 200000)
count = cond.sum()
print(count)

# set bpm
slow_low, slow_high, jog_low, jog_high, interval_low, interval_high = setup.set_bmp()

# split dataframes
music_speeds = setup.set_pace_music(music, slow_low, slow_high, jog_low, jog_high, interval_low, interval_high)

# run length and type
time = setup.set_time()
type = setup.set_type()

# create playlist
playlist = create.create_playlist(music_speeds, time, type)

pl_done = playlist[["track_name", "track_artist", "tempo"]]

print(pl_done.head(10))
