import json
import pandas as pd
from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import StringType, IntegerType, LongType, FloatType,DateType
from pyspark import SparkContext

sc = SparkContext()

x_topic_df = sc.read.parquet("s3a://meetupdf/topic_df")
lower_string = UserDefinedFunction(lambda x: x.lower(), StringType())
topic_df = x_topic_df.select(*[lower_string(column).alias(column) if column == 'topic' \
	else column for column in x_topic_df.columns]).cache()

def convert_to_pd(df):
	'''input: a sparksql dataframe
		output: a panda dataframe that has converted timestamp to datetime '''
	topic_pd = df.toPandas()
	topic_pd['datetime'] = pd.to_datetime(topic_pd['event_time'],unit = 'ms')
	topic_pd['date'] =  pd.DatetimeIndex(topic_pd['datetime']).date
	return topic_pd

def get_df_city(pd,city):
	return pd.ix[pd['group_city'] == city]

if __name__ == '__main__':
	topic_pd = convert_to_pd(topic_df)
	sf_pd = get_df_city(topic_pd,'San Francisco')
	sf_pd.write.parquet("s3a://meetupdf/sf_pd")
	print("Done")