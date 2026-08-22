# Hadoop MapReduce Word Count on Multiple Files

## Introduction

This experiment demonstrates how to execute the Hadoop MapReduce Word Count application on multiple input files stored in HDFS.

Multiple text files are uploaded to HDFS and processed collectively by the MapReduce Word Count program. The generated output is then analyzed to identify the most frequently occurring words.

## Objective

The objectives of this experiment are:

- To create multiple input text files.
- To create an HDFS input directory.
- To upload multiple files to HDFS.
- To verify the uploaded files.
- To execute the Hadoop MapReduce Word Count program.
- To view the generated word count output.
- To identify the three most frequently occurring words.

## Technologies Used

- Apache Hadoop
- HDFS
- YARN
- MapReduce
- Java
- Ubuntu / WSL

## Input Files

The following files are used:

- `file1.txt`
- `file2.txt`
- `file3.txt`

## Workflow

1. Start Hadoop services.
2. Create an HDFS input directory.
3. Create multiple text files.
4. Upload the files to HDFS.
5. Verify the uploaded files.
6. Execute the Hadoop Word Count program.
7. View the generated output.
8. Sort the output according to word frequency.
9. Identify the top three most frequent words.
10. Stop Hadoop services.

## Commands Used

### Start HDFS

```bash
start-dfs.sh
```

### Start YARN

```bash
start-yarn.sh
```

### Verify Services

```bash
jps
```

### Create HDFS Input Directory

```bash
hdfs dfs -mkdir -p /multiple_wordcount/input
```

### Upload Multiple Files

```bash
hdfs dfs -put file1.txt file2.txt file3.txt /multiple_wordcount/input/
```

### Verify Uploaded Files

```bash
hdfs dfs -ls /multiple_wordcount/input
```

### Run Word Count

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /multiple_wordcount/input /multiple_wordcount/output
```

### View Output

```bash
hdfs dfs -cat /multiple_wordcount/output/part-r-00000
```

### Sort Results by Frequency

```bash
hdfs dfs -cat /multiple_wordcount/output/part-r-00000 | sort -k2 -nr
```

### Display Top Three Words

```bash
hdfs dfs -cat /multiple_wordcount/output/part-r-00000 | sort -k2 -nr | head -3
```

## Expected Output

The MapReduce program processes all three input files together and produces a word frequency result.

The output is stored in:

`/multiple_wordcount/output`

The main output file is:

`part-r-00000`

The output can be sorted by frequency to identify the most frequently occurring words.

## Learning Outcomes

After completing this experiment, the following concepts are understood:

- Creating and managing directories in HDFS.
- Uploading multiple files to HDFS.
- Running MapReduce on multiple input files.
- Generating word frequency results.
- Sorting MapReduce output.
- Identifying frequently occurring words.
- Understanding distributed processing of multiple datasets.

## Result

The Hadoop MapReduce Word Count application was successfully executed on multiple input files. The files were stored in HDFS, processed collectively using MapReduce, and the resulting word frequencies were analyzed to identify the most frequently occurring words.

## Conclusion

This experiment demonstrates how Hadoop MapReduce can process multiple input files collectively and generate word frequency statistics. The results can be further analyzed using Linux commands to identify the most frequently occurring words.
