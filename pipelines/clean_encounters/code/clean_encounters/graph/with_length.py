from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_encounters.config.ConfigStore import *
from clean_encounters.udfs.UDFs import *

def with_length(spark: SparkSession, bronze_encounters: DataFrame) -> DataFrame:
    return bronze_encounters.select(
        col("Id"), 
        col("START"), 
        col("STOP"), 
        ((to_timestamp(col("STOP")).cast(LongType()) - to_timestamp(col("START")).cast(LongType())) / lit(3600)).alias(
          "LENGTH_HOURS"
        ), 
        col("PATIENT"), 
        col("PROVIDER"), 
        col("ENCOUNTERCLASS"), 
        col("CODE"), 
        col("DESCRIPTION"), 
        col("COST"), 
        col("REASONCODE"), 
        col("REASONDESCRIPTION")
    )
