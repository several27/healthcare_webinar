from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from ingest_conditions.config.ConfigStore import *
from ingest_conditions.udfs.UDFs import *

def bronze_conditions(spark: SparkSession, raw_conditions: DataFrame):
    raw_conditions.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.bronze_conditions")
