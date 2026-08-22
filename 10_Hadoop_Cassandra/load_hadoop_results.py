from cassandra.cluster import Cluster

cluster = Cluster(["127.0.0.1"])
session = cluster.connect("music_streaming")

daily_file = "output/daily_aggregates.txt"

with open(daily_file, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        parts = line.split("\t")

        if len(parts) != 3:
            continue

        date = parts[0]
        total_plays = int(parts[1])
        total_duration = int(parts[2])

        session.execute(
            """
            INSERT INTO daily_aggregates
            (date, total_plays, total_duration)
            VALUES (%s, %s, %s)
            """,
            (date, total_plays, total_duration)
        )

top_songs_file = "output/top_songs.txt"

with open(top_songs_file, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        parts = line.split("\t")

        if len(parts) != 2:
            continue

        song = parts[0]
        play_count = int(parts[1])

        session.execute(
            """
            INSERT INTO top_songs
            (song, play_count)
            VALUES (%s, %s)
            """,
            (song, play_count)
        )

print("Hadoop results loaded into Cassandra successfully.")

cluster.shutdown()
