# Hadoop Word Count Using MapReduce

## Introduction

This experiment demonstrates the implementation of the Word Count application using the Hadoop MapReduce framework.

The experiment involves creating an input text file, uploading it to HDFS, executing the Hadoop Word Count MapReduce program, and viewing the generated word frequency results.

## Objective

The objectives of this experiment are:

- To create a text file containing sample data.
- To upload the input file to HDFS.
- To execute the Hadoop MapReduce Word Count program.
- To generate the frequency of each word.
- To view the generated results from HDFS.

## Technologies Used

- Apache Hadoop
- HDFS
- YARN
- MapReduce
- Java
- Ubuntu / WSL

## Input File

The input file used in this experiment is:

`tech.txt`

The file contains sample information related to Artificial Intelligence, Machine Learning, Big Data, Hadoop, and Spark.

## Commands Used

### 1. Start HDFS

```bash
start-dfs.sh
```

### 2. Start YARN

```bash
start-yarn.sh
```

### 3. Check Hadoop Services

```bash
jps
```

### 4. Create HDFS Input Directory

```bash
hdfs dfs -mkdir -p /wordcount/input
```

### 5. Upload Input File to HDFS

```bash
hdfs dfs -put tech.txt /wordcount/input/
```

### 6. Verify Input File

```bash
hdfs dfs -ls /wordcount/input
```

### 7. Run Hadoop Word Count

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /wordcount/input /wordcount/output
```

### 8. Check Output Directory

```bash
hdfs dfs -ls /wordcount/output
```

### 9. Display Word Count Results

```bash
hdfs dfs -cat /wordcount/output/part-r-00000
```

## Expected Result

The MapReduce program processes the input file and produces an output containing each word along with its frequency.

The output is stored in the following HDFS directory:

`/wordcount/output`

The main result file is:

`part-r-00000`

## Learning Outcomes

After completing this experiment, the following concepts are understood:

- Hadoop MapReduce workflow.
- Uploading input data to HDFS.
- Executing a built-in MapReduce application.
- Generating word frequency results.
- Reading MapReduce output from HDFS.
- Understanding distributed data processing.

## Result

The Hadoop MapReduce Word Count application was successfully executed. The input file was stored in HDFS, processed using MapReduce, and the word frequency results were generated and stored in HDFS.

## Conclusion

This experiment provides a practical introduction to Hadoop MapReduce and demonstrates how text data can be processed using Hadoop MapReduce to generate word frequency information.
