from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_conditions.config.ConfigStore import *
from ingest_conditions.udfs.UDFs import *
from prophecy.utils import *
from ingest_conditions.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_conditions = raw_conditions(spark)
    bronze_conditions(spark, df_raw_conditions)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_conditions")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/ingest_conditions")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
