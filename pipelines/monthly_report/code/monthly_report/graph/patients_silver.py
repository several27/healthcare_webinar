from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def patients_silver(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.silver_patients")
