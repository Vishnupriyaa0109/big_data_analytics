#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split(",")

    if len(parts) != 6:
        continue

    try:
        user_id = parts[0]
        timestamp = parts[1]
        song = parts[2]
        artist = parts[3]
        session_id = parts[4]
        duration = int(parts[5])

        date = timestamp.split(" ")[0]

        print(f"{date}\t1\t{duration}")

    except ValueError:
        continue
