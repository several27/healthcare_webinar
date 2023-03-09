from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def OrderBy_1(spark: SparkSession, Aggregate_2: DataFrame) -> DataFrame:
    return Aggregate_2.orderBy(col("count").desc())
