
# HDFS Basic Commands

This experiment demonstrates the basic Hadoop Distributed File System (HDFS) commands used for creating directories, uploading files, viewing files, downloading files, and checking file replication.

## Prerequisites

- Apache Hadoop installed and configured
- HDFS services running
- Ubuntu/WSL terminal
- Access to the Hadoop command line
- Sample text files

## Objectives

- Create directories in HDFS.
- Upload files from the local system to HDFS.
- List files and directories stored in HDFS.
- Display the contents of HDFS files.
- Download files from HDFS to the local file system.
- Check the replication factor of HDFS files.

## Commands Used

### 1. Check HDFS

```bash
hdfs dfs -ls /
````

### 2. Create a Directory

```bash
hdfs dfs -mkdir /bigdata
```

### 3. Create a Subdirectory

```bash
hdfs dfs -mkdir /bigdata/input
```

### 4. List Directories

```bash
hdfs dfs -ls /bigdata
```

### 5. Upload a File to HDFS

```bash
hdfs dfs -put sample1.txt /bigdata/input/
```

### 6. Upload Multiple Files

```bash
hdfs dfs -put sample2.txt sample3.txt /bigdata/input/
```

### 7. List Uploaded Files

```bash
hdfs dfs -ls /bigdata/input
```

### 8. Display File Contents

```bash
hdfs dfs -cat /bigdata/input/sample1.txt
```

### 9. Display Multiple Files

```bash
hdfs dfs -cat /bigdata/input/sample2.txt
hdfs dfs -cat /bigdata/input/sample3.txt
```

### 10. Download a File from HDFS

```bash
hdfs dfs -get /bigdata/input/sample1.txt downloaded.txt
```

### 11. Verify the Downloaded File

```bash
cat downloaded.txt
```

### 12. Check File Information

```bash
hdfs dfs -ls -h /bigdata/input
```

### 13. Check Replication

```bash
hdfs dfs -stat %r /bigdata/input/sample1.txt
```

### 14. Display File Blocks and Locations

```bash
hdfs fsck /bigdata/input/sample1.txt -files -blocks -locations
```

## Learning Outcomes

After completing this experiment, the following HDFS operations can be performed:

* Directory creation
* Directory listing
* File uploading
* File viewing
* File downloading
* File information checking
* HDFS replication verification
* HDFS block and location inspection

## Result

The basic HDFS file and directory management operations were successfully performed using Hadoop commands.

````

The reference README covers essentially these same operations: directory creation, uploading, listing, viewing, downloading, and replication verification. :contentReference[oaicite:1]{index=1}

---

# 2. `sample1.txt`

Create:

```text
sample1.txt
````

Content:

```text
Big Data is the future of analytics
```

This matches the reference file. ([GitHub][2])

---

# 3. `sample2.txt`

Create:

```text
sample2.txt
```

Content:

```text
Hadoop processes large datasets efficiently
```

This matches the reference file. ([GitHub][3])

---

# 4. `sample3.txt`

Create:

```text
sample3.txt
```

Content:

```text
HDFS replicates data across multiple nodes
```

This matches the reference file. ([GitHub][4])

---

# 5. `downloaded.txt`

Create:

```text
downloaded.txt
```

Content:

```text
Big Data is the future of analytics
```

The reference repository has the same resulting content in `downloaded.txt`. ([GitHub][5])


