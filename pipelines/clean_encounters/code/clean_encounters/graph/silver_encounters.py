from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_encounters.config.ConfigStore import *
from clean_encounters.udfs.UDFs import *

def silver_encounters(spark: SparkSession, valid_reasons: DataFrame):
    valid_reasons.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .saveAsTable(f"lakehouse.silver_encounters")
