from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def gold_report(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.gold_patients")
