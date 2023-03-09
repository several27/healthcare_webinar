from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *

def Deduplicate_2(spark: SparkSession, OrderBy_1: DataFrame) -> DataFrame:
    return OrderBy_1.dropDuplicates(["CITY"])
