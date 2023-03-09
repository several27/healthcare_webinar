from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def Join_2(spark: SparkSession, patients: DataFrame, in1: DataFrame, ) -> DataFrame:
    return patients.alias("patients").join(in1.alias("in1"), (col("patients.Id") == col("in1.PATIENT")), "inner")
