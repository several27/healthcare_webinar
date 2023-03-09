from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def inpatient_only(spark: SparkSession, by_patient_id: DataFrame) -> DataFrame:
    return by_patient_id.filter((col("ENCOUNTERCLASS") == lit("inpatient")))
