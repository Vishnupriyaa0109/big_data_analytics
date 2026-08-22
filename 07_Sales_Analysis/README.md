# Sales Analysis using Hadoop MapReduce

## Introduction

This project demonstrates Sales Analysis using Hadoop MapReduce and Hadoop Streaming with custom Python Mapper and Reducer programs.

The project processes sales data stored in HDFS to calculate total sales for products, identify the Top 5 products based on total sales, and perform city-wise product analysis.

## Objective

The objectives of this project are:

- Analyze sales data using Hadoop MapReduce.
- Process large-scale sales data using Hadoop Streaming.
- Implement custom Python Mapper and Reducer programs.
- Calculate total sales for each product.
- Identify the Top 5 products based on total sales.
- Perform city-wise product sales analysis.

## Technologies Used

- Apache Hadoop
- HDFS
- YARN
- Hadoop Streaming
- MapReduce
- Python 3
- Java
- Ubuntu / WSL

## Dataset

The dataset contains the following fields:

| Field | Description |
|---|---|
| Date | Date of the transaction |
| Product | Product name |
| Sales Amount | Sales value of the product |
| City | City where the sale occurred |

Example:

```text
2024-01-01,Laptop,45000,Delhi
```

## Dataset Files

- `sales_products.txt` - Small sample dataset.
- `sales_products_large.txt` - Large dataset generated from the sample records.

## Workflow

1. Create the sales dataset.
2. Generate the large sales dataset.
3. Start Hadoop services.
4. Create an HDFS input directory.
5. Upload the sales dataset to HDFS.
6. Develop the product sales Mapper.
7. Develop the product sales Reducer.
8. Execute Hadoop Streaming.
9. Calculate total sales for each product.
10. Identify the Top 5 products.
11. Perform city-wise product analysis.
12. View the generated results.

## Product Sales Analysis

The product sales analysis uses:

- `mapper_top_products.py`
- `reducer_top_products.py`

The Mapper extracts the product and sales amount.

The Reducer groups the sales values for each product and calculates the total sales.

The products are then sorted by total sales to identify the Top 5 products.

## City-wise Product Analysis

The city-wise analysis uses:

`mapper_city_products.py`

The Mapper creates a combined key containing the city and product.

Example:

```text
Delhi_Laptop
Mumbai_Mouse
Bangalore_Keyboard
```

This allows sales information to be analyzed according to both city and product.

## Hadoop Commands

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
hdfs dfs -mkdir -p /sales_analysis/input
```

### Upload Dataset

```bash
hdfs dfs -put sales_products_large.txt /sales_analysis/input/
```

### Verify Dataset

```bash
hdfs dfs -ls /sales_analysis/input
```

## Hadoop Streaming

Find the Hadoop Streaming JAR:

```bash
ls $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar
```

Run the product sales analysis:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /sales_analysis/input/sales_products_large.txt \
-output /sales_analysis/output_top \
-mapper mapper_top_products.py \
-reducer reducer_top_products.py \
-file mapper_top_products.py \
-file reducer_top_products.py
```

View the results:

```bash
hdfs dfs -cat /sales_analysis/output_top/part-00000
```

## City-wise Analysis

Run:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /sales_analysis/input/sales_products_large.txt \
-output /sales_analysis/output_city \
-mapper mapper_city_products.py \
-reducer NONE \
-file mapper_city_products.py
```

View the output:

```bash
hdfs dfs -cat /sales_analysis/output_city/part-00000
```

## Expected Output

The product analysis generates a result similar to:

```text
TOP 5 PRODUCTS BY SALES:
========================================
1. Laptop: ...
2. Monitor: ...
3. Keyboard: ...
4. Mouse: ...
```

The exact values depend on the input dataset.

The city-wise analysis produces records containing the city, product, and corresponding sales amount.

## Learning Outcomes

After completing this project, the following concepts are understood:

- Hadoop Streaming architecture.
- Python Mapper programs.
- Python Reducer programs.
- HDFS data storage.
- Product-wise sales analysis.
- Total sales calculation.
- Top-selling product identification.
- City-wise product analysis.
- Distributed processing of large datasets.

## Project Structure

```text
07_Sales_Analysis/
│
├── README.md
├── 7 Sales Analysis using Hadoop MapReduce.txt
├── mapper_top_products.py
├── reducer_top_products.py
├── mapper_city_products.py
├── sales_products.txt
└── sales_products_large.txt
```

## Result

The sales dataset was successfully processed using Hadoop Streaming.

The project calculates product-wise total sales, identifies the Top 5 products, and generates city-wise product sales information.

## Conclusion

This project demonstrates the use of Hadoop MapReduce and Hadoop Streaming with Python for distributed sales data analysis.

The implementation provides practical experience in HDFS, Mapper and Reducer programs, product-wise aggregation, Top 5 analysis, and city-wise sales processing.

## License

This project is intended for educational and learning purposes.
