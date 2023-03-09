from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from covid_analysis.config.ConfigStore import *
from covid_analysis.udfs.UDFs import *
from prophecy.utils import *
from covid_analysis.graph import *

def pipeline(spark: SparkSession) -> None:
    df_patients = patients(spark)
    df_encounters = encounters(spark)
    df_Join_2 = Join_2(spark, df_patients, df_encounters)
    df_Reformat_1 = Reformat_1(spark, df_Join_2)
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_Aggregate_2 = Aggregate_2(spark, df_Filter_1)
    df_Filter_2 = Filter_2(spark, df_Aggregate_2)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_2)
    df_Deduplicate_2 = Deduplicate_2(spark, df_OrderBy_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/covid_analysis")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/covid_analysis")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
