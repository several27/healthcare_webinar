from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from clean_encounters.config.ConfigStore import *
from clean_encounters.udfs.UDFs import *
from prophecy.utils import *
from clean_encounters.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_encounters = bronze_encounters(spark)
    df_with_length = with_length(spark, df_bronze_encounters)
    df_valid_reasons = valid_reasons(spark, df_with_length)
    silver_encounters(spark, df_valid_reasons)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/clean_encounters")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/clean_encounters")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
