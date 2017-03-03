from pyspark.sql.functions import desc, explode
df = spark.read.json("s3a://tweet-firehose/2017/02/*/*/*")

df.printSchema()


group_df = df.select(df['group']['group_id'],df['group']['group_name'],df['group']['group_city'], df['group']['group_country'],df['group']['group_state']).distinct()

topic_df = df.select(df['group']['group_id'],explode(df['group']['group_topics']).alias("topic")).distinct()

event_df = df.select(df['event']['event_id'],df['event']['event_name'],df['event']['time'],df['event']['event_url'], df['venue']['venue_id']).distinct()

rsvp_df = df.select(df['rsvp_id'],df['member']['member_id'],df['event']['event_id'],df['mtime']).distinct()

#Save DataFrames to Parquet

group_df.write.parquet("s3a://meetupdf/group_df")
topic_df.write.parquet("s3a://meetupdf/topic_df")
event_df.write.parquet("s3a://meetupdf/event_df")
rsvp_df.write.parquet("s3a://meetupdf/rsvp_df")

#top 10 topics 

topic_count = topic_df.groupby('topic').count()
topic_count.orderBy(desc('count')).show(10)
