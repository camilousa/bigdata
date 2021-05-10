from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('count').getOrCreate()

input_data = spark.readStream.format('socket').option('host', 'localhost').option('port', 9897).load()

data = input_data.groupBy('value').count()

query = data.writeStream.outputMode('complete').format('console').start()

query.awaitTermination()
