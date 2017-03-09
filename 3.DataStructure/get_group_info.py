import pprint
import pandas as pd
import urllib
import requests
import json
import time
import codecs
import sys
import ssl
import boto
from boto.s3.connection import S3Connection
reload(sys)
sys.setdefaultencoding('utf-8')

def get_results(params):
	
	request = requests.get("http://api.meetup.com/2/groups",params=params)
	data = request.json()
	return data

def main(df):
	groups = df['group_id'].tolist()
	api_key= "2874d38771329205940487d21283d3e"
	group_id = []
	group_description = []
	topics = []

	for group in groups:
			response=get_results({"sign":"true","country":"US", "city":"San Francisco", \
								  "group_id": group, "state":"CA", "radius": 10, "key":api_key})
			if response.get('results'):
				result = response.get('results')
				for element in result:
					group_id.append(element['id'])
					group_description.append(element['description'])
					list_of_topics = [i['name'] for i in element['topics']]
					topics.append(list_of_topics)
					
	group_metadata = pd.DataFrame([group_id,group_description,topics]).T
	group_metadata.columns = ['group_id','group_description','topics']
	group_data = group_metadata.to_csv(None, header = None )

	return group_data


def boto_upload_s3(csv_file):
	conn = S3Connection(host='s3.amazonaws.com')
	new_bucket = conn.get_bucket('meetup_group_info')
	

	# website_bucket = conn.get_bucket('sparksubmitresults')
	output_file = new_bucket.new_key('group_info.csv')
	output_file.set_contents_from_string(csv_file, policy='public-read')

if __name__=="__main__":
	df = pd.read_csv('sf_csv.csv')
	group_data_csv = main(df)
	boto_upload_s3(group_data_csv)

		