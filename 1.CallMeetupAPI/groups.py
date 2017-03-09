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

def firehose():
	'''Input:None
	Output: For each city, return group info'''
	cities =[("Seattle","WA"),("Boston", "MA"),("San Jose", "CA"),
	("Los Angeles","CA"),("Denver","CO"),("Houston","TX"),("Portland","OR"),
	("Atlanta","GA"),("San Francisco","CA"),("New Haven","CT"),
	("Chicago","IL"),("New York","NY"),]
	api_key= "53747843757c2c115136274431417e9"
	while True:
		for (city, state) in cities:
			per_page = 500
			response=get_results({"sign":"true","country":"US", "city":city, "state":state,"radius": 10,"key":api_key, "page":per_page })
			for group in response['results']:
				dump_to_s3 = client.put_record(DeliveryStreamName='MeetUpGroupsStream',Record={'Data': group + '\chauchau'})
		time.sleep(1)

def get_results(params):

	request = requests.get("http://api.meetup.com/2/groups",params=params)
	data = request.json()
	return data

if __name__ == 	'__main__':	
	firehose()




