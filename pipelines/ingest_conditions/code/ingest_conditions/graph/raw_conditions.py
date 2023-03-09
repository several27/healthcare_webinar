from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from ingest_conditions.config.ConfigStore import *
from ingest_conditions.udfs.UDFs import *

def raw_conditions(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("START", StringType(), True), StructField("STOP", StringType(), True), StructField("PATIENT", StringType(), True), StructField("ENCOUNTER", StringType(), True), StructField("CODE", StringType(), True), StructField("DESCRIPTION", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/databricks-datasets/rwe/ehr/csv/conditions.csv")
