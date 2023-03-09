from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *

def by_patient_id(spark: SparkSession, patients_silver: DataFrame, in1: DataFrame, ) -> DataFrame:
    return patients_silver\
        .alias("patients_silver")\
        .join(in1.alias("in1"), (col("patients_silver.Id") == col("in1.PATIENT")), "inner")
