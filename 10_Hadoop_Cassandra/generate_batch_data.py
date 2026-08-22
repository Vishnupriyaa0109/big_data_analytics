import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "data/batch_plays.csv"
NUM_RECORDS = 100000

songs = [
    ("Blinding Lights", "The Weeknd"),
    ("Shape of You", "Ed Sheeran"),
    ("Believer", "Imagine Dragons"),
    ("Perfect", "Ed Sheeran"),
    ("Someone Like You", "Adele"),
    ("Havana", "Camila Cabello"),
    ("Levitating", "Dua Lipa"),
    ("Stay", "The Kid LAROI"),
    ("Bad Guy", "Billie Eilish"),
    ("Heat Waves", "Glass Animals")
]

start_date = datetime(2024, 1, 1)

with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)

    for i in range(NUM_RECORDS):
        user_id = f"user_{random.randint(1, 1000)}"

        timestamp = start_date + timedelta(
            minutes=random.randint(0, 60 * 24 * 30)
        )

        song, artist = random.choice(songs)

        session_id = f"session_{random.randint(1, 5000)}"

        duration = random.randint(120, 360)

        writer.writerow([
            user_id,
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            song,
            artist,
            session_id,
            duration
        ])

print(f"Generated {NUM_RECORDS} records in {OUTPUT_FILE}")
