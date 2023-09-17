def set_bmp():
    slow_low = 100
    slow_high = 105
    jog_low = 120
    jog_high = 125
    interval_low = 140
    interval_high = 145

    return slow_low, slow_high, jog_low, jog_high, interval_low, interval_high


def set_pace_music(music, slow_low, slow_high, jog_low, jog_high, interval_low, interval_high):
    music_speeds = {}

    # slow songs
    filter_slow = (music['tempo'] >= slow_low) & (music['tempo'] <= slow_high)
    slow_songs = music[filter_slow]

    # jog songs
    filter_jog = (music['tempo'] >= jog_low) & (music['tempo'] <= jog_high)
    jog_songs = music[filter_jog]

    # run songs
    filter_run = (music['tempo'] >= interval_low) & (music['tempo'] <= interval_high)
    run_songs = music[filter_run]

    music_speeds["slow_songs"] = slow_songs
    music_speeds["jog_songs"] = jog_songs
    music_speeds["run_songs"] = run_songs

    return music_speeds

def set_time():
    # set time in milliseconds (1800000 is 30mins)
    time = 1800000

    return time

def set_type():
    type = "equal_intervals"

    return type


