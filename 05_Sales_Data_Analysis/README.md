# Sales Data Analysis Using Hadoop

## Introduction

This experiment demonstrates the analysis of sales data using the Hadoop ecosystem. The sales dataset is stored in HDFS and processed using Hadoop MapReduce.

The dataset contains product, category, and sales amount information.

## Objective

The objectives of this experiment are:

- To create a sales dataset.
- To upload sales data to HDFS.
- To process sales data using Hadoop.
- To execute a MapReduce operation.
- To view the generated output.
- To understand how Hadoop can be used for sales data analysis.

## Technologies Used

- Apache Hadoop
- HDFS
- YARN
- MapReduce
- Java
- Ubuntu / WSL

## Dataset

The input file is:

`sales.txt`

The dataset contains the following fields:

| Field | Description |
|---|---|
| Product | Name of the product |
| Category | Product category |
| Sales | Sales amount |

## Hadoop Workflow

1. Start Hadoop services.
2. Create an HDFS input directory.
3. Upload the sales dataset to HDFS.
4. Verify the uploaded data.
5. Execute the MapReduce operation.
6. View the generated output.
7. Analyze the sales results.

## Commands Used

### Start HDFS

```bash
start-dfs.sh
```

### Start YARN

```bash
start-yarn.sh
```

### Check Hadoop Services

```bash
jps
```

### Create HDFS Input Directory

```bash
hdfs dfs -mkdir -p /sales/input
```

### Upload Sales Dataset

```bash
hdfs dfs -put sales.txt /sales/input/
```

### Verify Uploaded File

```bash
hdfs dfs -ls /sales/input
```

### Display Sales Data

```bash
hdfs dfs -cat /sales/input/sales.txt
```

### Run MapReduce

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /sales/input /sales/output
```

### View Output

```bash
hdfs dfs -ls /sales/output
```

```bash
hdfs dfs -cat /sales/output/part-r-00000
```

## Learning Outcomes

After completing this experiment, the following concepts are understood:

- Storing sales data in HDFS.
- Uploading datasets to HDFS.
- Processing data using Hadoop MapReduce.
- Viewing MapReduce output.
- Understanding distributed processing of sales data.

## Result

The sales dataset was successfully stored in HDFS and processed using Hadoop MapReduce. The generated output was successfully stored and retrieved from HDFS.

## Conclusion

This experiment demonstrates the use of Hadoop for processing sales-related data. It provides practical experience in storing datasets in HDFS and executing distributed processing using MapReduce.
