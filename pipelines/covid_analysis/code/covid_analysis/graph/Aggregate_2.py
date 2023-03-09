from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def Aggregate_2(spark: SparkSession, Filter_1: DataFrame) -> DataFrame:
    df1 = Filter_1.groupBy(col("REASONDESCRIPTION"), col("CITY"))

    return df1.agg(avg(col("length")).alias("length"), count(col("length")).alias("count"))
