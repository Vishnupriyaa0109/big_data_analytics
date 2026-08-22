# Apache Cassandra Exercise – Sparkify Music Streaming

## Overview

This project demonstrates Apache Cassandra data modeling using a music streaming dataset based on Sparkify.

The exercise focuses on query-based table design, inserting data, executing CQL queries, demonstrating UPSERT operations, and working with Cassandra consistency levels.

## Objective

The objectives of this exercise are:

- Create a Cassandra keyspace.
- Design query-specific tables.
- Insert sample records.
- Execute CQL queries.
- Demonstrate UPSERT functionality.
- Verify and change Cassandra consistency levels.

## Technologies Used

- Apache Cassandra
- Cassandra Query Language (CQL)
- cqlsh

## Project Structure

```text
09_Cassandra_Exercise/
├── README.md
└── 9 Cassandra Exercise.txt
```

## Steps Performed

### 1. Create Keyspace

```sql
CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': '1'
};
```

### 2. Use Keyspace

```sql
USE sparkify;
```

### 3. Create Tables

Three query-specific tables are created:

- `song_info_by_session`
- `song_playing_history_by_user`
- `who_listened_to_song`

### 4. Insert Sample Data

Sample records are inserted into the three tables using CQL `INSERT` statements.

### 5. Execute Queries

#### Query 1 — Song Information by Session

```sql
SELECT *
FROM song_info_by_session
WHERE session_id = 100;
```

#### Query 2 — User's Song Playing History

```sql
SELECT *
FROM song_playing_history_by_user
WHERE user_id = 1
AND session_id = 100;
```

#### Query 3 — Users Who Listened to a Song

```sql
SELECT *
FROM who_listened_to_song
WHERE song = 'Hey Jude';
```

## UPSERT Demonstration

Cassandra performs an UPSERT when an `INSERT` uses the same primary key as an existing row.

Example:

```sql
INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES
(100, 1, 'The Beatles', 'Let It Be', 4.03);
```

If the same primary key already exists, Cassandra updates the existing row instead of creating a duplicate row.

## Consistency Level

Check the current consistency level:

```sql
CONSISTENCY;
```

Set the consistency level to ONE:

```sql
CONSISTENCY ONE;
```

## Features Demonstrated

- Cassandra keyspace creation
- Query-driven data modeling
- Primary key design
- Data insertion
- CQL query execution
- UPSERT behavior
- Consistency level management

## Learning Outcomes

After completing this exercise, the following concepts are understood:

- Cassandra's query-first data modeling approach.
- Designing tables for specific queries.
- Using CQL for database operations.
- Cassandra UPSERT functionality.
- Cassandra consistency levels.
- Query-based table design.

## Result

The Cassandra exercise successfully demonstrates keyspace creation, query-specific table design, data insertion, CQL queries, UPSERT operations, and consistency-level management.

## Conclusion

This exercise provides practical experience with Apache Cassandra and demonstrates how its query-driven data modeling approach can be used for a music streaming application.

The exercise also demonstrates important Cassandra concepts such as primary keys, UPSERT behavior, CQL queries, and consistency levels.
