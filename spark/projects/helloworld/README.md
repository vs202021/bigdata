## What is this?

This is just a simple project which can be used as a starting skelton to start with sbt and spark-submit

1. Clone the repository:
```
	git clone https://github.com/cloudxlab/bigdata.git
	cd bigdata/spark/projects/helloworld
```
2. To run follow these steps:
```
	sbt package
	spark-submit target/scala-2.11/hello-world_2.11-1.0.jar
	# Or to run it in the yarn mode use
	spark-submit --master yarn target/scala-2.11/hello-world_2.11-1.0.jar
```

It should display something like:

	The Project Gutenberg EBook of The Adventures of Sherlock Holmesby Sir Arthur Conan Doyle(#15 in our series by Sir Arthur Conan Doyle)Copyright laws are changing all over the world. Be sure to check thecopyright laws for your country before downloading or redistributingthis or any other Project Gutenberg eBook.This header should be the first thing seen when viewing this ProjectGutenberg file.  Please do not remove it.  Do not change or edi


If you get an error like this:
---
hadoop.mapred.FileAlreadyExistsException: Output directory hdfs://cxln1.c.thelab-240901.internal:8020/user/sandeep/big_copy_spark already exists
	at org.apache.hadoop.mapred.FileOutputFormat.checkOutputSpecs(FileOutputFormat.java:131)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply$mcV$sp(PairRDDFunctions.scala:1191)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1168)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1168)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:151)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:112)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:362)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopDataset(PairRDDFunctions.scala:1168)
	
---
It is because the output direcory is already existing, please delete the output folder in HDFS using:

	hadoop fs -rmr big_copy_spark


