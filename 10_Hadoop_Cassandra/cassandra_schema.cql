CREATE KEYSPACE IF NOT EXISTS music_streaming
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};

USE music_streaming;

CREATE TABLE IF NOT EXISTS realtime_plays (
    user_id text,
    timestamp timestamp,
    song text,
    artist text,
    session_id text,
    duration int,
    PRIMARY KEY ((user_id), timestamp, session_id)
) WITH CLUSTERING ORDER BY (timestamp DESC);

CREATE TABLE IF NOT EXISTS daily_aggregates (
    date text,
    total_plays int,
    total_duration bigint,
    PRIMARY KEY (date)
);

CREATE TABLE IF NOT EXISTS top_songs (
    song text,
    play_count int,
    PRIMARY KEY (song)
);
