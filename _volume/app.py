from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col, avg, count

spark = SparkSession.builder.appName("AdvancedSeismicAnalysis").getOrCreate()
threshold = 0.5
data_path = "hdfs://namenode:8020/chemin/vers/votre/dataset.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

df = df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

daily_stats = df.groupBy("date").agg(avg("magnitude").alias("avg_magnitude"),
                                      count("secousse").alias("count_secousses"))

daily_stats.show()

from pyspark.sql.window import Window
from pyspark.sql.functions import lag, lead

windowSpec = Window.orderBy("date")

daily_stats = daily_stats.withColumn("prev_day_magnitude",
                                      lag(daily_stats["avg_magnitude"]).over(windowSpec))

daily_stats = daily_stats.withColumn("diff_magnitude",
                                      col("avg_magnitude") - col("prev_day_magnitude"))

increased_activity = daily_stats.filter(col("diff_magnitude") > threshold) 

increased_activity.show()

spark.stop()
