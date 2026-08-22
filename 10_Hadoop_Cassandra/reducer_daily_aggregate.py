#!/usr/bin/env python3

import sys

current_date = None
total_plays = 0
total_duration = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 3:
        continue

    date = parts[0]
    plays = int(parts[1])
    duration = int(parts[2])

    if current_date == date:
        total_plays += plays
        total_duration += duration

    else:
        if current_date is not None:
            print(
                f"{current_date}\t"
                f"{total_plays}\t"
                f"{total_duration}"
            )

        current_date = date
        total_plays = plays
        total_duration = duration

if current_date is not None:
    print(
        f"{current_date}\t"
        f"{total_plays}\t"
        f"{total_duration}"
    )
