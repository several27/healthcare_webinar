from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from ingest_patients.config.ConfigStore import *
from ingest_patients.udfs.UDFs import *

def bronze_patients_1(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable(f"lakehouse.bronze_patients")
