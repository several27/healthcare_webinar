from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_encounters.config.ConfigStore import *
from clean_encounters.udfs.UDFs import *

def bronze_encounters(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_encounters")
