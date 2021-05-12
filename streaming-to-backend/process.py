from pyspark.sql import SparkSession
from pyspark.sql import types
from pyspark.sql import functions as f
import requests

def process(row):
	print(30*'*')
	print('procesando...')
	datos = {'sensor': row['sensor'],'count': row['count']}	
	requests.post('http://127.0.0.1:5000/', data=datos)
	print(row)
	print(30*'*')


spark = SparkSession.builder.appName('window-processing').getOrCreate()

lines = spark.readStream.format('socket').option('host', 'localhost').option('port', '9898').load() 

col1 = f.split(lines.value, ',')[0].alias('sensor') 
col2 = f.split(lines.value, ',')[1].alias('dato')\
		.cast(types.IntegerType())

query = lines.select(col1, col2).groupBy('sensor')\
				.count()

program = query.writeStream.\
	foreach(process).\
	outputMode('complete').\
	start()

program.awaitTermination()



