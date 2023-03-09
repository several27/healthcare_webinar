from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from clean_conditions.config.ConfigStore import *
from clean_conditions.udfs.UDFs import *
from prophecy.utils import *
from clean_conditions.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_conditions = bronze_conditions(spark)
    silver_conditions(spark, df_bronze_conditions)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/clean_conditions")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/clean_conditions")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
