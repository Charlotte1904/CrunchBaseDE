#!/usr/bin/env/ python

import boto3
import json
import requests
import time
import codecs
import sys
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

# Connect to firehose
client = boto3.client('firehose',region_name = 'us-west-2')

def get_results(params):

	request = requests.get("http://api.meetup.com/2/groups",params=params)
	data = request.json()
	return data

def firehose():
	'''Input:None
	Output: For each city, return group info'''
	cities =[("Seattle","WA"),("Boston", "MA"),("San Jose", "CA"),("Denver","CO"),
	("Houston","TX"),("Portland","OR"),("Atlanta","GA"),("San Francisco","CA"),("Chicago","IL"),("New York","NY")]
	api_key= "53747843757c2c115136274431417e9"
	# print(cities)
	counter = 0
	while True:
		for (city, state) in cities:
			per_page = 500
			try: 
				response=get_results({"sign":"true","country":"US", "city":city, "state":state,"radius": 10,"key":api_key, "page":per_page })
				results = response['results']
				for group in results:
					dump_to_s3 = client.put_record(DeliveryStreamName='GroupsNewSplitter',Record={'Data': json.dumps(group) + '\chauchau'})
					counter += 1
					# print(counter)
			except:
				continue


if __name__ == 	'__main__':	
	while True:
		firehose()




