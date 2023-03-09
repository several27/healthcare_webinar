from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_conditions.config.ConfigStore import *
from clean_conditions.udfs.UDFs import *

def silver_conditions(spark: SparkSession, bronze_conditions: DataFrame):
    bronze_conditions.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.silver_conditions")
