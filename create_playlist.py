import random
import pandas as pd

def create_playlist(music_speeds, time, type):
    pass 

    walk = music_speeds["slow_songs"]
    jog = music_speeds["jog_songs"]
    run = music_speeds["run_songs"]

    playlist = []
    walk_nums = []
    jog_nums = []
    run_nums = []

    while len(walk_nums) < 5:
        n = random.randint(0, len(walk) - 1)
        if n not in walk_nums:
            walk_nums.append(n)
    else:
        # Replace duplicate with a new random number
        n = random.randint(0, len(walk) - 1)

    while len(run_nums) < 5:
        n = random.randint(0, len(run) - 1)
        if n not in run_nums:
            run_nums.append(n)
    else:
        # Replace duplicate with a new random number
        n = random.randint(0, len(run) - 1)

    playlist_df = pd.DataFrame(columns=walk.columns)  # Create a DataFrame with the same columns as 'walk'

    for i in range(5):
        # Alternate between walk and run, adding entire rows to the playlist_df
        playlist_df = playlist_df.append(walk.iloc[walk_nums[i]], ignore_index=True)
        playlist_df = playlist_df.append(run.iloc[run_nums[i]], ignore_index=True)

    return playlist_df