from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from ingest_encounters.config.ConfigStore import *
from ingest_encounters.udfs.UDFs import *

def bronze_encounters(spark: SparkSession, Source_0: DataFrame):
    Source_0.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.bronze_encounters")
