# Hadoop + Cassandra Integration

## Overview

This project demonstrates the integration of Apache Hadoop and Apache Cassandra for processing and storing large-scale music streaming data.

The project uses Hadoop MapReduce for batch processing and Cassandra for storing real-time and processed results.

The workflow combines:

- Cassandra for NoSQL data storage.
- Hadoop HDFS for distributed file storage.
- Hadoop Streaming for batch data processing.
- Python Mapper and Reducer programs.
- Cassandra for storing the final processed results.

## Objective

The objectives of this project are:

- Generate a large batch dataset containing music streaming records.
- Store data in HDFS.
- Process the batch dataset using Hadoop MapReduce.
- Calculate daily listening aggregates.
- Identify the top songs.
- Store Hadoop results in Cassandra.
- Demonstrate integration between Hadoop and Cassandra.

## Technologies Used

- Apache Hadoop
- HDFS
- Hadoop MapReduce
- Hadoop Streaming
- Apache Cassandra
- Docker
- Docker Compose
- Python
- CQL

## Project Architecture

```text
Music Streaming Data
        |
        +----------------------+
        |                      |
        v                      v
   Cassandra              Batch Dataset
   Real-time Data          100,000 Records
                               |
                               v
                             HDFS
                               |
                               v
                       Hadoop MapReduce
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
        Daily Aggregates              Top Songs
                 |                           |
                 +-------------+-------------+
                               |
                               v
                         Cassandra
                         Final Results
```

## Project Structure

```text
10_Hadoop_Cassandra/
│
├── README.md
├── docker-compose.yml
├── 10_Hadoop_Cassandra.txt
│
├── data/
│   ├── README.md
│   └── batch_plays.csv
│
├── scripts/
│   ├── cassandra_schema.cql
│   ├── generate_batch_data.py
│   ├── load_hadoop_results.py
│   ├── load_realtime_data.cql
│   ├── mapper_daily_aggregate.py
│   ├── reducer_daily_aggregate.py
│   ├── mapper_top_songs.py
│   ├── reducer_top_songs.py
│   └── run_hadoop_jobs.sh
│
└── output/
    ├── README.md
    ├── daily_aggregates.txt
    └── top_songs.txt
```

## Data

The batch dataset contains 100,000 music streaming records.

Each record contains:

- user_id
- timestamp
- song
- artist
- session_id
- duration

Example:

```text
user_1,2024-01-01 10:30:00,Song A,Artist A,session_1,245
```

## Step 1: Start Cassandra

Start the Cassandra container using Docker Compose:

```bash
docker compose up -d
```

Check the running containers:

```bash
docker ps
```

Check Cassandra logs:

```bash
docker logs cassandra
```

## Step 2: Create Cassandra Schema

Connect to Cassandra:

```bash
docker exec -it cassandra cqlsh
```

Execute the schema file:

```bash
docker exec -i cassandra cqlsh < scripts/cassandra_schema.cql
```

## Step 3: Generate Batch Dataset

Generate the large batch dataset:

```bash
python3 scripts/generate_batch_data.py
```

The generated dataset contains 100,000 records.

The file is:

```text
data/batch_plays.csv
```

## Step 4: Upload Dataset to HDFS

Create the HDFS input directory:

```bash
hdfs dfs -mkdir -p /hadoop_cassandra/input
```

Upload the dataset:

```bash
hdfs dfs -put data/batch_plays.csv /hadoop_cassandra/input/
```

Verify the uploaded file:

```bash
hdfs dfs -ls /hadoop_cassandra/input
```

## Step 5: Run Daily Aggregation

The daily aggregation MapReduce job calculates listening activity by day.

Run:

```bash
bash scripts/run_hadoop_jobs.sh
```

The generated daily aggregate output is stored in:

```text
output/daily_aggregates.txt
```

## Step 6: Run Top Songs Analysis

The top songs MapReduce job identifies the most frequently played songs.

The generated output is stored in:

```text
output/top_songs.txt
```

## Step 7: Load Hadoop Results into Cassandra

The Hadoop results can be loaded into Cassandra using:

```bash
python3 scripts/load_hadoop_results.py
```

## Step 8: Verify Cassandra Results

Connect to Cassandra:

```bash
docker exec -it cassandra cqlsh
```

Use the appropriate keyspace and query the processed tables to verify that the Hadoop results have been stored successfully.

## MapReduce Processing

### Daily Aggregation

The daily aggregation Mapper extracts the date and listening duration from each record.

The Reducer aggregates the values for each date.

### Top Songs

The top songs Mapper extracts the song and its play information.

The Reducer aggregates the number of plays and identifies the most frequently played songs.

## Output

The project produces two main analytical outputs:

### Daily Aggregates

Daily listening activity calculated from the batch dataset.

### Top Songs

The most frequently played songs from the dataset.

## Learning Outcomes

After completing this project, the following concepts are understood:

- Hadoop HDFS.
- Hadoop MapReduce.
- Hadoop Streaming.
- Python Mapper and Reducer programs.
- Cassandra data modeling.
- Docker-based Cassandra deployment.
- Batch data processing.
- Real-time and batch data integration.
- Loading Hadoop results into Cassandra.
- Distributed data processing.

## Result

The Hadoop and Cassandra integration was successfully demonstrated.

The large music streaming dataset was generated, stored in HDFS, processed using Hadoop MapReduce, and the resulting analytical data was prepared for storage in Cassandra.

## Conclusion

This project demonstrates how Hadoop and Cassandra can be integrated to build a distributed data processing pipeline.

Hadoop provides distributed storage and batch processing capabilities, while Cassandra provides scalable NoSQL storage for processed and real-time data.

The combination provides a practical architecture for handling large-scale music streaming analytics.
