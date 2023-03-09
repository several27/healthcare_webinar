from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from clean_encounters.config.ConfigStore import *
from clean_encounters.udfs.UDFs import *

def valid_reasons(spark: SparkSession, with_length: DataFrame) -> DataFrame:
    return with_length.filter(col("REASONDESCRIPTION").isNotNull())
