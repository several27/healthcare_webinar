from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "average_length_hours",
        concat(format_string("%.1f", col("average_length_hours")), lit(" minutes"))
    )
