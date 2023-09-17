import random

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



    playlist = [walk[walk_nums[0]], run[run_nums[0]],
                walk[walk_nums[1]], run[run_nums[1]],
                walk[walk_nums[2]], run[run_nums[2]],
                walk[walk_nums[3]], run[run_nums[3]],
                walk[walk_nums[4]], run[run_nums[4]]]

    return playlist