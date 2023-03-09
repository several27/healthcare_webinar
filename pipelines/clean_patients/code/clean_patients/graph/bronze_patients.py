from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_patients.config.ConfigStore import *
from clean_patients.udfs.UDFs import *

def bronze_patients(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_patients")
