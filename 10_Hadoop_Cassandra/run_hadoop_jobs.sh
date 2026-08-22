#!/bin/bash

INPUT="/hadoop_cassandra/input/batch_plays.csv"

DAILY_OUTPUT="/hadoop_cassandra/output/daily_aggregates"

TOP_SONGS_OUTPUT="/hadoop_cassandra/output/top_songs"

STREAMING_JAR=$(find "$HADOOP_HOME/share/hadoop/tools/lib" -name "hadoop-streaming*.jar" | head -1)

echo "Starting Hadoop Cassandra processing..."

echo "Removing old output directories..."

hdfs dfs -rm -r -f "$DAILY_OUTPUT"
hdfs dfs -rm -r -f "$TOP_SONGS_OUTPUT"

echo "Running daily aggregation..."

hadoop jar "$STREAMING_JAR" \
-input "$INPUT" \
-output "$DAILY_OUTPUT" \
-mapper "mapper_daily_aggregate.py" \
-reducer "reducer_daily_aggregate.py" \
-file "mapper_daily_aggregate.py" \
-file "reducer_daily_aggregate.py"

echo "Running top songs analysis..."

hadoop jar "$STREAMING_JAR" \
-input "$INPUT" \
-output "$TOP_SONGS_OUTPUT" \
-mapper "mapper_top_songs.py" \
-reducer "reducer_top_songs.py" \
-file "mapper_top_songs.py" \
-file "reducer_top_songs.py"

echo "Hadoop processing completed."

echo "Daily Aggregates:"
hdfs dfs -cat "$DAILY_OUTPUT/part-00000"

echo "Top Songs:"
hdfs dfs -cat "$TOP_SONGS_OUTPUT/part-00000"
