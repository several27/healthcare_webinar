from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_patients.config.ConfigStore import *
from clean_patients.udfs.UDFs import *

def silver_patients(spark: SparkSession, bronze_patients: DataFrame):
    bronze_patients.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.silver_patients")
