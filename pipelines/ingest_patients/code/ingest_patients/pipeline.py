from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_patients.config.ConfigStore import *
from ingest_patients.udfs.UDFs import *
from prophecy.utils import *
from ingest_patients.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_patients = raw_patients(spark)
    bronze_patients_1(spark, df_raw_patients)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_patients")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/ingest_patients")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
