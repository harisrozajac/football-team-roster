def who_plays(team: [str], interval: int, players_playing: int, game_duration: int, players_coming_in: int):
    """
    :param team: all players on a team
    :param interval: number of intervals for subbing
    :param players_playing: number of players that plays
    :param game_duration: duration of game in minutes
    :param players_coming_in: number of players that comes in each interval
    :return: players playing and subbing per each interval
    """

    full_data = []
    playing = team[0:players_playing]
    bench = team[players_playing:len(team)]
    final_team = None
    for i in range(1, interval + 1):
        interval_time_start = round(game_duration / interval * (i - 1))
        interval_time_end = round(game_duration / interval * i)
        if i == 1:
            final_team = \
                f'{interval_time_start}-{interval_time_end} | ' \
                f'playing: {playing} | bench: {bench}\n'
        else:
            final_team = \
                final_team + f'{interval_time_start}-{interval_time_end} | ' \
                             f'playing: {playing} | bench: {bench}\n'
        full_data.append({
            'interval': f'{interval_time_start}-{interval_time_end}',
            'playing': playing,
            "bench": bench
        })
        come_in = bench[:players_coming_in]
        bench = bench[players_coming_in:] + playing[:players_coming_in]
        playing = playing[players_coming_in:]
        for player in come_in:
            playing.append(player)
    return full_data


attack = ["Jose", "Josue", "Haris", "Abel", "Omar"]
defence = ["Alberto", "Kyle", "Tony", "Jared", "Rob"]

full_attack_per_interval = who_plays(attack, 8, 2, 40, 2)
full_defence_per_interval = who_plays(defence, 8, 3, 40, 2)

for a in range(0, len(full_attack_per_interval)):
     print(full_attack_per_interval[a]["interval"],
          "defence: ",
          full_defence_per_interval[a]["playing"],
          "attack: ",
          full_attack_per_interval[a]["playing"],
          '*** bench: ',
          "defence",
          full_defence_per_interval[a]["bench"],
          "attack: ",
          full_attack_per_interval[a]["bench"]
         )
