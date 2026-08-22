#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split(",")

    if len(parts) != 6:
        continue

    song = parts[2]

    print(f"{song}\t1")
