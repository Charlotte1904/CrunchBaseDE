import boto3
import json
import requests


# Connect to firehose
client = boto3.client('firehose',region_name = 'us-west-2')



#Loading meetup rsvp to the firehose
def firehose():
	iterator = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
	counter = 0
	for raw_rsvp in iterator.iter_lines():
		if raw_rsvp:
			response = client.put_record(DeliveryStreamName='MeetupRsvpStream',
				Record={'Data': (raw_rsvp+'\n')})
			counter += 1
		# if counter % 2 == 0:
		# 	print('Inserted {} events'.format(counter))
			




if __name__ == 	'__main__':	
	while True:
		firehose()



	