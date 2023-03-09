from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def sum_encounters(spark: SparkSession, inpatient_only: DataFrame) -> DataFrame:
    df1 = inpatient_only.groupBy(col("CITY"), col("REASONDESCRIPTION"))

    return df1.agg(count(col("LENGTH_HOURS")).alias("visits"), first(col("LENGTH_HOURS")).alias("average_length_hours"))
