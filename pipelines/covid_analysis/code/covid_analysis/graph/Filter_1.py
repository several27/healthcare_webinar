from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def Filter_1(spark: SparkSession, Reformat_1: DataFrame) -> DataFrame:
    return Reformat_1.filter(col("REASONDESCRIPTION").isNotNull())
