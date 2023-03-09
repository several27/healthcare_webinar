from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def Reformat_1(spark: SparkSession, Aggregate_1: DataFrame) -> DataFrame:
    return Aggregate_1.select(
        ((to_timestamp(col("STOP")).cast(LongType()) - to_timestamp(col("START")).cast(LongType())) / lit(3600)).alias(
          "length"
        ), 
        col("REASONDESCRIPTION"), 
        col("CITY")
    )
