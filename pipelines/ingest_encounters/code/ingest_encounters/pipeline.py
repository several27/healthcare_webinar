from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_encounters.config.ConfigStore import *
from ingest_encounters.udfs.UDFs import *
from prophecy.utils import *
from ingest_encounters.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_encounters = raw_encounters(spark)
    bronze_encounters(spark, df_raw_encounters)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_encounters")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/ingest_encounters")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
