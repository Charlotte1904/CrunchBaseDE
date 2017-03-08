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
	cities =[("San Francisco","CA"),("New Haven","CT"),("Chicago","IL"),("New York","NY"),("Seattle","WA")]
	api_key= "53747843757c2c115136274431417e9"
	while True:
		for (city, state) in cities:
			per_page = 10000
			response=get_results({"sign":"true","country":"US", "city":city, "state":state,"radius": 10,"key":api_key, "page":per_page })
			for group in response['results']:
				dump_to_s3 = client.put_record(DeliveryStreamName='MeetUpGroupsStream',Record={'Data': json.dumps(group) + '\n'})
		time.sleep(1)


if __name__ == 	'__main__':	
	firehose()




