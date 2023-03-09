from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from clean_patients.config.ConfigStore import *
from clean_patients.udfs.UDFs import *
from prophecy.utils import *
from clean_patients.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_patients = bronze_patients(spark)
    silver_patients(spark, df_bronze_patients)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/clean_patients")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/clean_patients")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
