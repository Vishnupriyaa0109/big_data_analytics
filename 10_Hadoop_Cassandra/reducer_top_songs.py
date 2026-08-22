#!/usr/bin/env python3

import sys

current_song = None
play_count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 2:
        continue

    song = parts[0]
    count = int(parts[1])

    if current_song == song:
        play_count += count

    else:
        if current_song is not None:
            print(f"{current_song}\t{play_count}")

        current_song = song
        play_count = count

if current_song is not None:
    print(f"{current_song}\t{play_count}")
