# Uncomment the following in CloudxLab Lab if you can't import pyspark in Python3.

# import os
# import sys
# os.environ["SPARK_HOME"] = "/usr/hdp/current/spark2-client"
# os.environ["PYLIB"] = os.environ["SPARK_HOME"] + "/python/lib"
# os.environ["PYSPARK_PYTHON"] = "/usr/local/anaconda/bin/python" 
# os.environ["PYSPARK_DRIVER_PYTHON"] = "/usr/local/anaconda/bin/python"
# sys.path.insert(0, os.environ["PYLIB"] +"/py4j-0.10.4-src.zip")
# sys.path.insert(0, os.environ["PYLIB"] +"/pyspark.zip")

# 

from pyspark.sql.types import Row

textRDD = sc.textFile("/data/spark/people.txt")

arrayRDD = textRDD.map(lambda x: x.split(","))

rowRDD = arrayRDD.map(lambda arr: Row(name=arr[0], age=int(arr[1].strip())))

peopleDF = rowRDD.toDF()
peopleDF.show()
