from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from monthly_report.config.ConfigStore import *
from monthly_report.udfs.UDFs import *
from prophecy.utils import *
from monthly_report.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_encounters = silver_encounters(spark)
    df_patients_silver = patients_silver(spark)
    df_by_patient_id = by_patient_id(spark, df_patients_silver, df_silver_encounters)
    df_inpatient_only = inpatient_only(spark, df_by_patient_id)
    df_sum_encounters = sum_encounters(spark, df_inpatient_only)
    df_cleanup_visits = cleanup_visits(spark, df_sum_encounters)
    gold_report(spark, df_cleanup_visits)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/monthly_report")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/monthly_report")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
