from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_conditions.config.ConfigStore import *
from clean_conditions.udfs.UDFs import *

def bronze_conditions(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_conditions")
