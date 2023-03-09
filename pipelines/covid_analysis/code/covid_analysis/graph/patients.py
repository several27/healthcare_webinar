from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def patients(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Id", StringType(), True), StructField("BIRTHDATE", StringType(), True), StructField("DEATHDATE", StringType(), True), StructField("SSN", StringType(), True), StructField("DRIVERS", StringType(), True), StructField("PASSPORT", StringType(), True), StructField("PREFIX", StringType(), True), StructField("FIRST", StringType(), True), StructField("LAST", StringType(), True), StructField("SUFFIX", StringType(), True), StructField("MAIDEN", StringType(), True), StructField("MARITAL", StringType(), True), StructField("RACE", StringType(), True), StructField("ETHNICITY", StringType(), True), StructField("GENDER", StringType(), True), StructField("BIRTHPLACE", StringType(), True), StructField("ADDRESS", StringType(), True), StructField("CITY", StringType(), True), StructField("STATE", StringType(), True), StructField("ZIP", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/databricks-datasets/rwe/ehr/csv/patients.csv")
