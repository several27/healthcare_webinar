from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def cleanup_visits(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_cleanup = cleanup(spark, in0)

    return df_cleanup
