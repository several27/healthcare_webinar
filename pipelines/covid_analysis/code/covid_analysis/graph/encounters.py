from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def encounters(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Id", StringType(), True), StructField("START", StringType(), True), StructField("STOP", StringType(), True), StructField("PATIENT", StringType(), True), StructField("PROVIDER", StringType(), True), StructField("ENCOUNTERCLASS", StringType(), True), StructField("CODE", StringType(), True), StructField("DESCRIPTION", StringType(), True), StructField("COST", StringType(), True), StructField("REASONCODE", StringType(), True), StructField("REASONDESCRIPTION", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/databricks-datasets/rwe/ehr/csv/encounters.csv")
